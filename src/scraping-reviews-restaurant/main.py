import json
import pathlib
from lib import pathList_ind
from lib import browser
import pandas as pd
import time
import csv

def main():
    # configファイル取得
    fp = pathlib.Path(__file__).parents[2]/"ignore"/"config.json"
    with open(fp, "r", encoding="utf-8") as file:
        configData = json.load(file)

    # 個別ページのパス取得
    driverList = pathList_ind.PathList_ind( config=configData , head=True )
    bookPathList = driverList.get_path_list()

    # 個別ページアクセス、書籍情報取得
    stores = list()
    driver = browser.Browser(True)
    page = driver.new_page()
    for i , b in enumerate(bookPathList) :
        page.goto(b)
        time.sleep(1)
        result = pd.Series()
        for table in  page.locator(configData["targetPages"]).all() :
            for tr in table.locator("tr").all() :
                key = tr.locator("th").first.inner_text()
                value = tr.locator("td").first.inner_text()
                result[key] = value
        stores.append(result)
    
    # ドライバクローズ
    driver.close()

    # 書籍情報保存
    outputPath = ( pathlib.Path(__file__).parent / pathlib.Path(configData["outputPath"]) ).resolve()
    outputPath.mkdir(parents=True , exist_ok=True)
    pd.DataFrame(stores) \
        .set_index("店名") \
            .to_csv(outputPath/"output.csv",quoting=csv.QUOTE_ALL)


if __name__ == "__main__":
    main()
