import re
import requests
from bs4 import BeautifulSoup


def extract_info(soup, link):
    title = None
    year = None
    millage = None
    transmission = None
    horsepower = None
    color = None
    

    div_with_margin = soup.find('div', style='margin-top:17px;')

    table = div_with_margin.find('table')
    
    title_h1 = soup.find('h1')
    
    title = title_h1.text.strip()

    price_div = soup.find('span' , id="details_price")
    
    price_text = price_div.text.strip()
    
    price_numbers = re.findall(r'\d+', price_text)
    
    price = ''.join(price_numbers)
    
    main_image_holder = soup.find('img', id="bigPictureCarousel")
    
    image = main_image_holder.get('src')
    
    images_holder = soup.find('div', id="pictures_moving_details_small")
    
    a_elements = images_holder.find_all('a')
    
    image_urls = []

    for a_element  in a_elements:
        image = a_element.get('data-link')
        if image:
            image_urls.append(image)
            
    more_info_specs = soup.find('ul', class_="dilarData")
    
    li_elements = more_info_specs.find_all('li')

    label_to_index = {
        "year": 1,
        "fuel_type": 3,
        "horsepower": 5,
        "transmission": 9,
        # "type": 11,
        "millage": 13,
        "color": 15,
    }

    specs_dict = {}  

    for label, index in label_to_index.items():
        info_value = li_elements[index].text.strip()
        specs_dict[label] = info_value
        

    return {
        'url': link,
        'title': title,
        'price': price,
        'main_image': image,
        'image_urls': image_urls,
        **{key: value for key, value in specs_dict.items() if key in ('year', 'fuel_type', 'horsepower', 'transmission', 'millage', 'color')}
        
    }
def scrape_single_ad_mobile(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        info = extract_info(soup, url)
        return info

    except requests.exceptions.RequestException as e:
        print(f"Error dokato se opitva da scrapne datata:  {e}")
        return None