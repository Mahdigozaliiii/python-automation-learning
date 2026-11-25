import time
import csv
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def scrape_digikala():
    url = "https://www.digikala.com/search/category-notebook-netbook-ultrabook/"
    print("Opening Edge browser...")
    options = Options()
    driver = webdriver.Edge(options=options)

    # لیستی برای ذخیره اطلاعات محصولات
    scraped_data = []

    try:
        driver.get(url)
        print("Waiting for products to load...")

        wait = WebDriverWait(driver, 20)
        product_class = "styles-module-scss-module__IjzMIG__ProductList__item"
        products = wait.until(EC.presence_of_all_elements_located(
            (By.CLASS_NAME, product_class)))

        print(f"Found {len(products)} products. Extracting data...\n")

        for product in products:
            try:
                # پیدا کردن اسم
                title = product.find_element(By.TAG_NAME, "h3").text
                if not title:
                    title = product.find_element(By.TAG_NAME, "h2").text

                # پیدا کردن قیمت
                try:
                    price = product.find_element(
                        By.CSS_SELECTOR, "span[data-testid='price-final']").text
                except:
                    price = "نامشخص"

                # اضافه کردن به لیست
                scraped_data.append({"Title": title, "Price": price})

                # فقط ۳۰ کاراکتر اول رو چاپ میکنه تا ترمینال شلوغ نشه
                print(f"Extracted: {title[:30]}...")

            except Exception as e:
                continue

        # ذخیره در فایل CSV
        if scraped_data:
            filename = "digikala_laptops.csv"
            with open(filename, mode='w', newline='', encoding='utf-8-sig') as file:
                writer = csv.DictWriter(file, fieldnames=["Title", "Price"])
                writer.writeheader()
                writer.writerows(scraped_data)
            print(
                f"\n✅ Successfully saved {len(scraped_data)} products to {filename}")
        else:
            print("\n❌ No data was scraped.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()
        print("Browser closed.")


if __name__ == "__main__":
    scrape_digikala()
