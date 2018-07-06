import requests
from bs4 import BeautifulSoup
import fileinput


from function import *


"""
c_name_1 | c_name_2 | score | c_code_1 | c_code_2
c_name_1 | c_name_2 | score | c_code_1 | c_code_2
"""
count_rows = 0

page = requests.get('https://www.fifa.com/worldcup/matches/?#knockoutphase')
soup = BeautifulSoup(page.content, 'html.parser')

date = soup.find_all('div', class_="fi-mu__info__datetime")

now = getNow()
print("now: {}".format(now))


result_arr = []
rows = soup.find_all('div', class_="fi-mu result")
# Find scheduled game
for row in rows:
    row_date = row.find('div', class_="fi-mu__info__datetime")
    row_date = row_date.text.strip()
    row_date = get_nth_line(row_date, 0)
    row_date = get_first_n_words(row_date, 3)
    # Today games
    if row_date == now:
        count_rows += 1
        c_name = row.find_all('span', class_="fi-t__nText")
        c_name_1 = c_name[0].text
        c_name_2 = c_name[1].text

        score = row.find('span', class_="fi-s__scoreText").text
        score = score.strip()
        try:
            score = time.strptime(score, '%H:%M')
            score = 'Soon'
        except ValueError:
            score = " ".join(score)
        c_code_1 = convert_name_to_code(c_name_1)
        c_code_2 = convert_name_to_code(c_name_2)
        temp_arr = [c_name_1, c_name_2, score, c_code_1, c_code_2]
        result_arr.append(temp_arr)
# Find live game
rows = soup.find_all('div', class_="fi-mu live")
for row in rows:
    row_date = row.find('div', class_="fi-mu__info__datetime")
    row_date = row_date.text.strip()
    row_date = get_nth_line(row_date, 0)
    row_date = get_first_n_words(row_date, 3)

    if row_date == now:
        count_rows += 1
        c_name = row.find_all('span', class_="fi-t__nText")
        c_name_1 = c_name[0].text
        c_name_2 = c_name[1].text

        score = row.find('span', class_="fi-s__scoreText").text
        score = score.strip()
        try:
            score = time.strptime(score, '%H:%M')
            score = 'Soon'
        except ValueError:
            score = " ".join(score)
        c_code_1 = convert_name_to_code(c_name_1)
        c_code_2 = convert_name_to_code(c_name_2)
        temp_arr = [c_name_1, c_name_2, score, c_code_1, c_code_2]
        result_arr.append(temp_arr)
# Find Finished game
rows = soup.find_all('div', class_="fi-mu fixture")
for row in rows:
    row_date = row.find('div', class_="fi-mu__info__datetime")
    row_date = row_date.text.strip()
    row_date = get_nth_line(row_date, 0)
    row_date = get_first_n_words(row_date, 3)

    if row_date == now:
        count_rows += 1
        c_name = row.find_all('span', class_="fi-t__nText")
        c_name_1 = c_name[0].text
        c_name_2 = c_name[1].text

        score = row.find('span', class_="fi-s__scoreText").text
        score = score.strip()
        try:
            score = time.strptime(score, '%H:%M')
            score = 'Soon'
        except ValueError:
            score = " ".join(score)
        c_code_1 = convert_name_to_code(c_name_1)
        c_code_2 = convert_name_to_code(c_name_2)
        temp_arr = [c_name_1, c_name_2, score, c_code_1, c_code_2]
        result_arr.append(temp_arr)

# Write into HTML
fh = open('./2018_WORLDCUP_MATCHBOARD.html', 'w', encoding='utf-8')
datetime_now = now
fh.write('<!--@2_WORLDCUP_MATCHBOARD_' + datetime_now + '(start)@-->\n')
fh.write('<table class="table-standings">\n')
fh.write('<tbody>\n')
# If there is no game
if count_rows == 0:
    fh.write('<tr>\n')
    fh.write('<td class="table_score">\n')
    fh.write('<p>No game today.</p>\n')
    fh.write('</td>\n')
# When there is a game
for arr in result_arr:
    fh.write('<tr>\n')
    fh.write('<td class="table-home">\n')
    fh.write('<p><span>' + arr[0] + '</span><span class="flag-icon flag-icon-' + arr[3] +'"></span></p>\n')
    fh.write('</td>\n')
    fh.write('<td class="table-score">\n')
    fh.write('<span class="eng">' + arr[2] + '</span>\n')
    fh.write('</td>\n')
    fh.write('<td class="table-away">\n')
    fh.write('<p><span class="flag-icon flag-icon-' + arr[4] +'"></span><span>' + arr[1] + '</span></p>\n')
    fh.write('</td>\n')
    fh.write('</tr>\n')
fh.write('</tbody>\n')
fh.write('</table>\n')
fh.write('<!--@2_WORLDCUP_MATCHBOARD_' + datetime_now + '(end)@-->\n')
