import time
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

    try:
        driver.get(url)
        print("Waiting for products to load...")

        # صبر می‌کنیم تا کارت‌های محصول واقعاً در صفحه ظاهر بشن
        wait = WebDriverWait(driver, 20)

        # این کلاس رو از خروجی ترمینال خودت پیدا کردیم
        product_class = "styles-module-scss-module__IjzMIG__ProductList__item"
        products = wait.until(EC.presence_of_all_elements_located(
            (By.CLASS_NAME, product_class)))

        print(f"Found {len(products)} products. Extracting data...\n")

        for product in products[:5]:
            try:
                # پیدا کردن اسم محصول (معمولاً داخل تگ h3 یا h2 است)
                title = product.find_element(By.TAG_NAME, "h3").text
                if not title:
                    title = product.find_element(By.TAG_NAME, "h2").text

                # پیدا کردن قیمت
                try:
                    price = product.find_element(
                        By.CSS_SELECTOR, "span[data-testid='price-final']").text
                except:
                    # روش جایگزین برای پیدا کردن قیمت
                    price = product.text.split("\n")[-1]

                print(f"Title: {title}")
                print(f"Price: {price}")
                print("-" * 30)
            except Exception as e:
                # اگر یکی از محصولات ساختارش فرق داشت، ازش رد میشیم
                continue

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()
        print("Browser closed.")


if __name__ == "__main__":
    scrape_digikala()
