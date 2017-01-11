import urllib
from bs4 import BeautifulSoup
import requests
import xlwt
import string
from stem_filter import strip_names
import unicodedata


def get_micro_data(names_list, username, password):
    s = requests.Session()
    s.post('https://www.micromedexsolutions.com/home/dispatch/PFDefaultActionId/pf.LoginAction',
           data = {'login.username_index_0' : username, 'login.password_index_0' : password,
                   'submit':'login'})

    r = s.get('http://www.micromedexsolutions.com/micromedex2/librarian/CS/456B51/ND_PR/evidencexpert/ND_P/evidencexpert/DUPLICATIONSHIELDSYNC/F79C55/ND_PG/evidencexpert/ND_B/evidencexpert/ND_AppProduct/evidencexpert/ND_T/evidencexpert/PFActionId/evidencexpert.ProductSearch?navitem=topToxDrugLookup&isToolPage=true')

    micro_data = {line:{} for line in names_list}
    micro_data["DYMs"] = {}

    for line in names_list:
        line_names = strip_names(line)

        for name in line_names:
            micro_data[line][name] = {}
            m = s.get(
            "http://www.micromedexsolutions.com/micromedex2/librarian/CS/D1A629/ND_PR/evidencexpert/ND_P/evidencexpert/DUPLICATIONSHIELDSYNC/6270A7/ND_PG/evidencexpert/ND_B/evidencexpert/ND_AppProduct/evidencexpert/ND_T/evidencexpert/PFActionId/evidencexpert.ShowProductSearchResults?SearchTerm=" + name + "&searchType=Tox-Tool-Product-Substance&searchContent=MARTINDALE"
            )
            soup = BeautifulSoup(m.text, "html.parser")
            table = soup.find(id="PSN_Table")

            if table:
                trs = soup.find(id="PSN_Table").find("tbody").find_all("tr")

                for tr in trs:
                    tds = tr.find_all("td")
                    hit_country = ""
                    hit_manufacturer = ""
                    hit_name = tds[1].text.strip(string.whitespace)
                    hit_country += tds[3].text.replace(u'\xa0', u' ').strip(string.whitespace)
                    hit_manufacturer += tds[2].text.replace(u'\xa0', u' ').strip(string.whitespace)
                    #print name, hit_name, hit_manufacturer, hit_country
                    if "[" in hit_name:
                        hit_name = hit_name.split("[")[0].strip(string.whitespace)
                        hit_country = "FM " + hit_country
                        hit_manufacturer = "FM " + hit_manufacturer

                    if hit_name not in micro_data[line][name]:
                        micro_data[line][name][hit_name] = []

                    if hit_country[3:]:
                        micro_data[line][name][hit_name].append("".join([hit_country]))
                    else:
                        micro_data[line][name][hit_name].append("".join([hit_manufacturer]))

            # CHECK FOR DID YOU MEANS
            dym = soup.findAll("div", { "class" : "pdxDidYouMean" })#.findAll("a")
            if dym:
                micro_data["DYMs"][str(name)] = True
                #TODO search also for 'Did ypu mean's and add date to existing name conflicts
            else:
                micro_data["DYMs"][str(name)] = False

    return micro_data

def micro_excel_doc(names, data):
    workbook = xlwt.Workbook()

    h_style = xlwt.easyxf('font: name Verdana, bold True; align: vert centre, \
        horiz centre; borders: left thin, top thin, bottom thin, right thin')
    t_style = xlwt.easyxf('font: name Verdana, bold False; align: vert centre, \
        wrap on; borders: left thin, top thin, bottom thin, right thin')

    # Set up sheet 1
    sheet1 = workbook.add_sheet("Micromedex Results", cell_overwrite_ok=True)
    sheet1.write(0, 0, "Name", style=h_style)
    sheet1.write(0, 1, "Names Screened", style=h_style)
    sheet1.write(0, 2, "Conflicts", style=h_style)
    sheet1.col(0).width = 18 * 256
    sheet1.col(1).width = 18 * 256
    sheet1.col(2).width = 80 * 256
    sheet1.row(0).height = 1000

    row_count = 1
    for name_rationale in names:
        names_rationale_cell = name_rationale
        names_on_line_cell = " \ ".join(data[name_rationale])
        conflicts_cell = ""

        for name_on_line in data[name_rationale]:
            for conflict_name in data[name_rationale][name_on_line]:
                countries = ", ".join(data[name_rationale][name_on_line][conflict_name])
                conflicts_cell += "".join([conflict_name, " (", countries, "); "])

        sheet1.write(row_count, 0, names_rationale_cell, t_style)
        sheet1.write(row_count, 1, names_on_line_cell, t_style)
        sheet1.write(row_count, 2, conflicts_cell.strip("; "), t_style)
        sheet1.row(row_count).height_mismatch = True
        sheet1.row(row_count).height = 1000
        row_count += 1

        workbook.save("micro_data.xls")


if __name__=="__main__":
    #For testing
    names = ["Avostim", "Ciantis", "Vyigro"]
    get_micro_data(names, "asdasf", "dfdf")
