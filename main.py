# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests

# https://www.thepythoncode.com/article/use-google-custom-search-engine-api-in-python
# Search operators https://de.semrush.com/blog/google-suchoperatoren/
# Query parameters https://developers.google.com/custom-search/v1/reference/rest/v1/cse/list#request

# # get the API KEY here: https://developers.google.com/custom-search/v1/overview
# # get your Search Engine ID on your CSE control panel
from config import *

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Starting, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    print_hi('DactaTrace Search')

    # using the first page
    page = 1
    # constructing the URL
    # doc: https://developers.google.com/custom-search/v1/using_rest
    # calculating start, (page=2) => (start=11), (page=3) => (start=21)
    start = (page - 1) * 10 + 1

    #############################################################################

    # building search queries

    # query = "python"

    # query = 'inurl:nzz.ch intext:marcel schlatter'  # documents that contain either Marcel OR Schlatter (or both)
    # query = 'inurl:shn.ch intext:marcel wenger'  # documents that contain either Marcel OR Wenger (or both)
    # query = 'inurl:weltwoche.ch intext:mörgeli'  #
    # query = 'inurl:weltwoche.ch intext:editorial köppel'  #
    # url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&sort=date"   # sort descending (newest first)
    # url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&sort={'date:r:20150101:20160101'}"   # date restriction https://support.google.com/programmable-search/thread/36978586/which-parameters-i-can-use-in-lowrange-and-highrange-in-custom-search-json-api?hl=en
    # url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&dateRestrict={'d100'}&sort=date"   # last 100 days https://support.google.com/programmable-search/thread/36978586/which-parameters-i-can-use-in-lowrange-and-highrange-in-custom-search-json-api?hl=en
    # url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&dateRestrict={'d100'}&sort=date:a"   # last 100 days https://support.google.com/programmable-search/thread/36978586/which-parameters-i-can-use-in-lowrange-and-highrange-in-custom-search-json-api?hl=en

    # query = 'inurl:nzz.ch'
    # query = 'inurl:shn.ch'
    # query = 'inurl:weltwoche.ch'
    # exactSearchTerm = 'mörgeli'
    # url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&exactTerms={exactSearchTerm}&sort=date"
    # url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&exactTerms={exactSearchTerm}&sort={'date:r:20150101:20160101'}" # results from 2015
    # url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&exactTerms={exactSearchTerm}&sort={'date:r:20221001:20221002'}" # results from yesterday and today (IF today is October 2, 2022)

    # exactSearchTerm = {'Kantonsrat Schaffhausen'}
    # query = 'inurl:sh.ch/CMS/get/file' # only exactSearchTerms
    # url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&exactTerms={exactSearchTerm}&sort=date"

    # exactSearchTerm = {'Kantonsrat Schaffhausen'}
    # query = 'inurl:sh.ch/CMS/get/file'  # additional search terms: uncomment ONE(!) of the lines below
    # query = query + " " + "förderprogramm AND kinderbetreuung AND Hausarztmedizin"
    # query = query + " " + "förderprogramm AND kinderbetreuung AND Hausarztmedizin AND Vorschulalter"
    # query = query + " " + "förderprogramm AND (kinderbetreuung OR Energie)"
    # url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&exactTerms={exactSearchTerm}&sort=date"

    # query = 'site:sh.ch filetype:pdf intitle:Protokoll'
    # query = query + " " + 'energiewende AND IPCC' # optional alternative 1
    # query = query + " " + 'energiewende' # optional alternative 2
    # query = query + " " + 'energiewende OR PUK' # optional alternative 2
    # exactSearchTerm = {'Kantonsrat Schaffhausen'}
    # url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&exactTerms={exactSearchTerm}&sort=date"

    # query = 'site:sh.ch filetype:pdf intitle:Amtsblatt' # no exactSearchTerm
    # query = query + " " + 'Arbeitszeitverordnung AND Schulferien' # optional alternative 1
    # query = query + " " + 'Arbeitszeitverordnung' # optional alternative 2
    # query = query + " " + 'Arbeitszeitverordnung OR Arbeitsamt' # optional alternative 2
    # url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&sort=date"
    # url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&sort={'date:r:20150101:20210101'}" # results from 2015 until 2020

    # query = 'site:sh.ch filetype:pdf intitle:Amtsblatt'
    # exactSearchTerm = 'während den Schulferien'
    # query = query + " " + 'Arbeitszeitverordnung AND Schulferien' # optional alternative 1
    # query = query + " " + 'Arbeitszeitverordnung' # optional alternative 2
    # query = query + " " + 'Arbeitszeitverordnung OR Arbeitsamt' # optional alternative 2
    # url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&sort=date&exactTerms={exactSearchTerm}"
    # url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&sort={'date:r:20150101:20210101'}&exactTerms={exactSearchTerm}" # results from 2015 until 2020

    # query = 'site:entscheidsuche.ch filetype:pdf'
    # exactSearchTerm = 'ZGB'
    # exactSearchTerm = 'Bundesstrafgericht'
    # exactSearchTerm = 'Arbeitszeit'
    # query = query + " " + 'Art. 314a AND Vertretung' # optional alternative 1
    # query = query + " " + 'Art. 314a' # optional alternative 1
    # query = query + " " + 'Gefährdung' # optional alternative 1
    # query = query + " " + 'Arbeitszeitverordnung' # optional alternative 2
    # query = query + " " + 'Arbeitszeitverordnung OR Arbeitsamt' # optional alternative 2
    # url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&sort=date&exactTerms={exactSearchTerm}"
    # url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&sort={'date:r:20200101:20210101'}&exactTerms={exactSearchTerm}" # results from 2015 until 2020

    # query = 'site:oereblex.sg.ch unterschutzstellungf'
    # query = 'site:oereblex.sh.ch unterschutzstellungf'
    # query = 'site:oereblex.tg.ch unterschutzstellungf'
    # query = 'site:oereblex.gr.ch unterschutzstellungf'
    # query = 'inurl:oereblex grenzabstand'
    # query = 'inurl:oereblex gestaltungsplan'
    # query = 'inurl:oereblex grenzabstand'
    # query = 'inurl:oereblex perimeter'

    # query = 'inurl:oereblex (baureglement OR bauordnung OR Baugesetz OR Zonenplan OR Nutzungsplan OR Schutzplan OR Perimeter OR Nutzungsordnung OR Gebührenreglement OR Gebührenordnung)'
    # query = 'inurl:st.gallen.tlex.ch (baureglement OR bauordnung OR Baugesetz OR Zonenplan OR Nutzungsplan OR Schutzplan OR Perimeter OR Nutzungsordnung OR Gebührenreglement OR Gebührenordnung)'
    # query = 'inurl:st.gallen.tlex.ch (baureglement OR bauordnung OR Baugesetz OR Zonenplan OR Nutzungsplan OR Schutzplan OR Perimeter OR Nutzungsordnung OR Gebührenreglement OR Gebührenordnung) AND "Bauordnung"' # optional zusätzlicher Fokus auf Baordnung
    query = 'inurl:st.gallen.tlex.ch (baureglement OR bauordnung OR Baugesetz OR Zonenplan OR Nutzungsplan OR Schutzplan OR Perimeter OR Nutzungsordnung OR Gebührenreglement OR Gebührenordnung) intitle:Bauordnung' # optional noch stärkerer Fokus auf Baordnung
    # exactSearchTerm = 'graubünden'
    # exactSearchTerm = 'schaffhausen'
    # exactSearchTerm = 'thurgau'
    # exactSearchTerm = 'bischofszell'
    # exactSearchTerm = 'thayngen'
    exactSearchTerm = 'st.gallen'
    url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&sort=date&exactTerms={exactSearchTerm}"
    # url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&sort=date"
    # url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&sort={'date:r:20200101:20210101'}&exactTerms={exactSearchTerm}"  # results from 2015 until 2020

    # query = 'inurl:oereblex gebührenordnung'
    # query = 'inurl:oereblex zonenplan'
    # query = 'inurl:oereblex perimeter'
    #
    # query = 'site:oereblex.sg.ch unterschutzstellungf'
    # query = 'site:oereblex.sg.ch baureglement'
    # query = 'site:oereblex.sg.ch unterschutzstellungf'
    # query = 'site:oereblex.sg.ch unterschutzstellungf'
    # query = 'site:oereblex.sg.ch unterschutzstellungf'
    # query = 'site:oereblex.sg.ch unterschutzstellungf'
    #
    # query = 'site:.ch intitle: gemeinde aadorf baureglement filetype:pdf'
    #
    # query = 'site:.ch intitle: gemeinde kreuzlingen abgabenordnung OR gebührenordnung filetype:pdf'
    # query = 'site:.ch intitle: rechtsbuch kreuzlingen filetype:pdf'
    #
    # query = 'inurl:.ch(rechtsbuch OR gesetzgebung) (gemeinde OR stadt) kreuzlingen filetype:pdf'
    # query = 'inurl:st.gallen.tlex.ch filetype:pdf' # Systematische Rechtssammlung der Stadt St. Gallen
    # query = 'inurl:srl.lu.ch filetype:pdf' # Systematische Rechtssammlung von Luzern
    # query = 'inurl:lawa.lu.ch filetype:pdf gewässerschutz' # Systematische Rechtssammlung von Luzern
    #
    # query 'inurl: admin.ch filetype:pdf erbrecht'
    #
    # query 'inurl:bj.admin.ch filetype:pdf erbrecht'
    # query 'inurl:bfe.admin.ch filetype:pdf erbrecht'
    # query 'inurl:bag.admin.ch filetype:pdf erbrecht'
    # query 'inurl:eda.admin.ch filetype:pdf erbrecht'
    # query 'inurl:ejpd.admin.ch filetype:pdf erbrecht'
    # query 'inurl:vbs.admin.ch filetype:pdf erbrecht'
    # query 'inurl:wbf.admin.ch filetype:pdf erbrecht'
    #
    # query = 'inurl:fedlex.admin.ch' # Systematische Rechtssammlung des Bundes
    #
    # query = 'inurl:epfl.ch/about/overview/fr/reglements-et-directives/polylex'  # Rechtssammlung der EPFL (französisch und englisch)
    #
    # query =  'inurl:rechtssammlung.sp.ethz.ch' # Rechtssammlung der ETH Zürich
    #
    # query = 'inurl:zh.ch wirtschaftsregister'
    # query = 'inurl:lu.ch wirtschaftsregister'
    # query = 'inurl:sg.ch filetype:pdf bussen'
    #
    # query = 'site: alexandria.unisg.ch/*' # Universität St. Gallen, Forschungsplattform Alexandria



    ################ bis dahin getestet ##############################3



    # query = 'inurl:sh.ch/CMS/get/file heizöl ' # documents that contain all three terms
    # query = 'inurl:sh.ch/CMS/get/file ' # documents that contain all three terms
    # query = 'inurl:sh.ch/CMS/get/file Transparenzinitiative Obergericht' # documents that either one of these, or both terms
    # query = '' # all documents that contain the exactSearchTerm 'Kantonsrat Schaffhausen'
    # exactSearchTerms = ['Kantonsrat Schaffhausen', 'protokoll']
    # url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&exactTerms={exactSearchTerm}&sort=date"
    # url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&start={start}&exactTerms={exactSearchTerms}&sort=date"

    # query = 'site:sh.ch filetype:pdf intitle:Protokoll  '
    # url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&exactTerms={exactSearchTerm}&sort=date"

    # query = 'inurl:srl.lu.ch'
    # query = 'site:sh.ch filetype:pdf intitle:amtsblatt tamagni falken'
    # query = 'site:sh.ch filetype:pdf intitle:amtsblatt tamagni OR falken'
    # query = 'site:sh.ch filetype:pdf intitle:amtsblatt tamagni'
    # query = 'site:sh.ch/CMS/get/file kantonsrat protokoll'
    # query = 'inurl:sh.ch/CMS/get/file kantonsrat protokoll'






    # url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}"
    # url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&sort=date"   # sort descending (newest first)
    # url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&sort=date:a" # sort ascending (oldest first)
    # url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&sort={'date:r:20180101:20230101'}"   # date restriction https://support.google.com/programmable-search/thread/36978586/which-parameters-i-can-use-in-lowrange-and-highrange-in-custom-search-json-api?hl=en
    # url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&dateRestrict={'d300'}"   # last 300 days https://support.google.com/programmable-search/thread/36978586/which-parameters-i-can-use-in-lowrange-and-highrange-in-custom-search-json-api?hl=en

    # url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&exactTerms={exactSearchTerm}"

    print("Request URL: ", url)
    # make the API request
    # https://developers.google.com/custom-search/v1/using_rest
    data = requests.get(url).json()

    # get the result items
    search_items = data.get("items")
    try: # iterate over 10 results found
        for i, search_item in enumerate(search_items, start=1):
            try:
                long_description = search_item["pagemap"]["metatags"][0]["og:description"]
            except KeyError:
                long_description = "N/A"
            # get the page title
            title = search_item.get("title")
            # page snippet
            snippet = search_item.get("snippet")
            # alternatively, you can get the HTML snippet (bolded keywords)
            html_snippet = search_item.get("htmlSnippet")
            # extract the page url
            link = search_item.get("link")
            # print the results
            print("=" * 10, f"Result #{i + start - 1}", "=" * 10)
            print("Title:", title)
            print("Snippet:", snippet)
            print("Long description:", long_description)
            print("URL:", link, "\n")
            print("*")
    except:
        print("*** empty search result list ***")


