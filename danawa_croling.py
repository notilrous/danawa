import requests
from bs4 import BeautifulSoup
import re
import time

base_URL = "https://prod.danawa.com"
URL = "https://m.danawa.com/sectionMain.html?code="
final_URL = "https://prod.danawa.com/list/?cate="
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0'
}
start_time = time.time()


def load_first_category():
    res_base = requests.get(base_URL, timeout=5, headers=headers)
    if res_base.status_code == 200:
        # 첫 카테고리
        soup = BeautifulSoup(res_base.text, 'html.parser')
        category_list = soup.findAll('a', {'class': 'category__list__btn', 'role': 'button'})
        items = {}
        category_code_list = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        for x, y in zip(category_list, category_code_list):
            items[y] = x.text
        # print(items)
        link_list = [
            "https://previews.123rf.com/images/tiurin1/tiurin11611/tiurin1161100011/69341303-%EB%83%89%EC%9E%A5%EA%B3%A0%EC%9D%98-%EC%83%81%EC%A7%95%EC%9E%85%EB%8B%88%EB%8B%A4-%EC%83%81-%EB%9D%BC%EC%9D%B8-%EC%95%84%ED%8A%B8-%EB%B2%A1%ED%84%B0-%EC%9D%BC%EB%9F%AC%EC%8A%A4%ED%8A%B8.jpg",
            "https://png.pngtree.com/png-clipart/20220603/ourlarge/pngtree-laptop-with-transparent-screen-png-image_4817269.png",
            "https://previews.123rf.com/images/onston/onston1509/onston150900004/45723154-%EB%85%B8%ED%8A%B8%EB%B6%81-%ED%83%9C%EB%B8%94%EB%A6%BF-pc-%ED%9C%B4%EB%8C%80-%EC%A0%84%ED%99%94-%EB%B2%A1%ED%84%B0-%EC%9D%BC%EB%9F%AC%EC%8A%A4%ED%8A%B8-%EB%A0%88%EC%9D%B4-%EC%85%98.jpg",
            "https://i.pinimg.com/550x/cb/88/34/cb8834c38a9609f8b3c446baaaf515bd.jpg",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRnKamAmccYrnluuLCpn5LZaxir0q8H0_MABQ&usqp=CAU",
            "https://us.123rf.com/450wm/yupiramos/yupiramos1709/yupiramos170906107/85138922-%EB%9E%A8%ED%94%84-%EC%A0%84%EA%B5%AC-%EC%A1%B0%EB%AA%85-%EA%B0%80%EA%B5%AC-%EC%A0%84%EA%B8%B0-%EC%9E%A5%EC%8B%9D-%EC%9A%94%EC%86%8C-%EB%B2%A1%ED%84%B0-%EC%9D%BC%EB%9F%AC%EC%8A%A4%ED%8A%B8-%EB%A0%88%EC%9D%B4%EC%85%98.jpg",
            "https://logoyogo.com/web/wp-content/uploads/edd/2020/12/logoyogo-1-41.jpg",
            "https://media.istockphoto.com/id/1302487421/ko/%EB%B2%A1%ED%84%B0/%EA%B1%B4%EA%B0%95%ED%95%9C-%EC%9D%BC%EC%83%81-%EC%83%9D%ED%99%9C-%EA%B0%9C%EB%85%90-%EB%B2%A1%ED%84%B0-%EB%A7%8C%ED%99%94-%EC%9D%BC%EB%9F%AC%EC%8A%A4%ED%8A%B8%EB%A1%9C-%EB%B0%94%EB%8B%A5%EC%97%90-%EB%A7%A4%ED%8A%B8%EC%97%90-%EC%A7%91%EC%97%90%EC%84%9C-%EC%9A%B4%EB%8F%99%EC%9D%84-%ED%95%98%EB%8A%94-%EC%A0%8A%EC%9D%80-%EC%97%AC%EC%84%B1.jpg?s=1024x1024&w=is&k=20&c=5QnfUSQHzZqJ529ib-7WSTTGPzgVlMgz-ZnT_jmkDb8=",
            "https://i.pinimg.com/originals/0b/ab/c8/0babc82b7b1a18e8d4617614589a2253.jpg",
            "https://image.idus.com/image/files/5b72292a39f64ed39127b2c17cebf698_720.jpg"]
        result = {}
        # print(items.values())
        for x, y, z in zip(items.values(), link_list, category_code_list):
            result[x] = {
                'code': z,
                'link': y
            }
        # print(result)
        return result


def load_second_category(code_num):
    res_base = requests.get(base_URL, timeout=5, headers=headers)
    res_URL = requests.get(URL + code_num, timeout=5, headers=headers)
    if res_base.status_code == 200:
        # 두번째 카테고리
        soup1 = BeautifulSoup(res_URL.text, 'html.parser')
        In_category_list = soup1.findAll('button', {'role': 'menuitem', 'class': 'button__category'})
        sec_img_list = soup1.select('button > span.box__image > img')
        # print(sec_img_list)
        # print(In_category_list)
        id_list = {}
        for x in In_category_list:
            id_list[x.text] = x["id"]
        # print(id_list)
        id1 = list(id_list.values())
        sec_list = {}
        for i in range(len(id1)):
            sec_category = soup1.select(f'#{id1[i]} > span.text__name')
            for x in sec_category:
                sec_list[i] = x.text
        last_sec_list = {}
        sec_img_dir = {}
        a = 0
        for x in sec_img_list:
            sec_img_dir[a] = x['src']
            a += 1
        # print(sec_img_dir)
        for x, y in zip(sec_list.values(), sec_img_dir.values()):
            last_sec_list[x] = {
                'link': y
            }
        return last_sec_list


def load_third_category(category_num, code_num):
    res_base = requests.get(base_URL, timeout=5, headers=headers)
    res_URL = requests.get(URL + code_num, timeout=5, headers=headers)
    if res_base.status_code == 200:
        soup1 = BeautifulSoup(res_URL.text, 'html.parser')
        Last_category_value_list = soup1.findAll('div', {'class': 'box__sub-category', 'role': 'region'})
        items2 = {}
        for x, y in enumerate(Last_category_value_list):
            items2[x] = y["id"]
        links = {}
        Detail_list = soup1.select(f'#{items2[int(category_num)]} > ul > li > a')
        for x in Detail_list:
            links[x.text] = x['href']
        return links

def load_prod(link):
    slice_num = re.findall(r'\d+', link)
    res = requests.get(final_URL + str(slice_num[0]), timeout=5, headers=headers)

    if res.status_code == 200:
        result_list = {}
        soup = BeautifulSoup(res.text, 'html.parser')
        for i in range(3):
            prod = list(soup.select(
                f'ul.product_list > li.prod_item:nth-of-type({i + 1}) > div.prod_main_info > div.prod_info > p.prod_name > a'))[
                0]
            prod_img = list(soup.select(
                f'ul.product_list > li.prod_item:nth-of-type({i + 1}) > div.prod_main_info > div.thumb_image > a > img'))[
                0]
            prod_spec = list(soup.select(
                f'ul.product_list > li.prod_item:nth-of-type({i + 1}) > div.prod_main_info > div.prod_info > dl.prod_spec_set > dd > div.spec_list'))[
                0]

            name = (prod.text.replace('\t', '').replace('\n', ''))
            url = (prod['href'])
            img = (prod_img['src'])
            spec = (prod_spec.text.replace('\n', ''))
            # print(name,url,img,spec)
            result_list[name] = {
                'url': url,
                'img': img,
                'spec': spec
            }
        # print("--- %s seconds ---" % (time.time() - start_time))
        return result_list
