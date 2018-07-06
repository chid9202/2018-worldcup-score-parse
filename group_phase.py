import requests
from bs4 import BeautifulSoup
from datetime import datetime
from function import *

"""
| country name_1 | MP_1 | W_1 | D_1 | L_1 | GF_1 | GA_1 | PTS_1 | f_code_1 |
| country name_2 | MP_2 | W_2 | D_2 | L_2 | GF_2 | GA_2 | PTS_2 | f_code_2 |
| country name_3 | MP_3 | W_3 | D_3 | L_3 | GF_3 | GA_3 | PTS_3 | f_code_3 |
| country name_4 | MP_4 | W_4 | D_4 | L_4 | GF_4 | GA_4 | PTS_4 | f_code_4 |
"""
class Group:
    def __init__(self, table, alphbet):
        self.group = 'Group ' + alphbet
        self.table = table;
        w, h = 9, 4
        self.scoreboard = [['r' for x in range(w)] for y in range(h)]
        self.setValues(self.table)

    def setValues(self, table):
        for i in range(0,4):
            # name
            name = table.find_all('span', class_='fi-t__nText ')
            name = name[i]
            self.scoreboard[i][0] = name.text
            # match played
            matchPlayed = table.find_all('td', class_='fi-table__matchplayed')
            matchPlayed = matchPlayed[i].find_all('span', class_='text')
            matchPlayed = matchPlayed[0]
            self.scoreboard[i][1] = matchPlayed.text
            # Win
            win = table.find_all('td', class_='fi-table__win')
            win = win[i].find_all('span', class_='text')
            win = win[0]
            self.scoreboard[i][2] = win.text
            # Draw
            draw = table.find_all('td', class_='fi-table__draw')
            draw = draw[i].find_all('span', class_='text')
            draw = draw[0]
            self.scoreboard[i][3] = draw.text
            # Lost
            lost = table.find_all('td', class_='fi-table__lost')
            lost = lost[i].find_all('span', class_='text')
            lost = lost[0]
            self.scoreboard[i][4] = lost.text
            # Goal for
            goalfor = table.find_all('td', class_='fi-table__goalfor')
            goalfor = goalfor[i].find_all('span', class_='text')
            goalfor = goalfor[0]
            self.scoreboard[i][5] = goalfor.text
            # Goal against
            goalagainst = table.find_all('td', class_='fi-table__goalagainst')
            goalagainst = goalagainst[i].find_all('span', class_='text')
            goalagainst = goalagainst[0]
            self.scoreboard[i][6] = goalagainst.text
            # Points
            pts = table.find_all('td', class_='fi-table__pts')
            pts = pts[i].find_all('span', class_='text')
            pts = pts[0]
            self.scoreboard[i][7] = pts.text
            self.scoreboard[i][8] = convert_name_to_code(self.scoreboard[i][0])

    def getCountry(self, row):
        return self.scoreboard[row][0]
    def getMP(self, row):
        return self.scoreboard[row][1]
    def getW(self, row):
        return self.scoreboard[row][2]
    def getD(self, row):
        return self.scoreboard[row][3]
    def getL(self, row):
        return self.scoreboard[row][4]
    def getPTS(self, row):
        return self.scoreboard[row][7]
    def getCountryCode(self, row):
        return self.scoreboard[row][8]
    # arrange countries in order by rank
    def getTop2(self):
        ret_arr = [None, None]
        first = second = -2147483648
        first_i = None
        second_i = None
        pts_arr = [int(self.scoreboard[0][7]), int(self.scoreboard[1][7]), int(self.scoreboard[2][7]), int(self.scoreboard[3][7])]
        for i in range(len(pts_arr)):
            if(pts_arr[i] > first):
                second = first
                second_i = first_i
                first = pts_arr[i]
                first_i = i
            # NOTE When index is between first and second
            elif ( pts_arr[i] > second and pts_arr[i] != first ):
                second = pts_arr[i]
                second_i = i

        # NOTE When there is no scond largest
        if (second == -2147483648):
            ret_arr[0] = first
            return ret_arr

        # NOTE When there is no largest
        elif (first == -2147483648):
            return ret_arr

        # NOTE When there are largest and second largest
        else:
            ret_arr[0] = first
            ret_arr[1] = second
            return ret_arr

    def writeHTML(self):
        fh = open('./scoreboard_' + self.group.replace(" ", "") + '.html', 'w', encoding='utf-8')
        datetime_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        fh.write('<!--@2_WORLDCUP_' + datetime_now + '(start)@-->\n')
        fh.write('<div class="slide_st item">\n')
        fh.write('<p class="caption_title eng">' + self.group + '</p>\n')
        fh.write('<div class="ma_top10">\n')
        fh.write('<table class="table-standings">\n')
        fh.write('<thead>\n')
        fh.write('<tr>\n')
        fh.write('<th class="table-teamname"></th>\n')
        fh.write('<th class="table-win"><span title="Won">W</span></th>\n')
        fh.write('<th class="table-draw"><span title="Draw">D</span></th>\n')
        fh.write('<th class="table-lost"><span title="Lost">L</span></th>\n')
        fh.write('<th class="table-pts"><span title="Points">WP</span></th>\n')
        fh.write('</tr>\n')
        fh.write('</thead>\n')
        fh.write('<tbody>\n')
        top_arr = self.getTop2()
        for i in range(0,4):
            # NOTE if i is in top 2
            if top_arr[0] == i or top_arr[1] == i:
                fh.write('<tr class="winner-team">\n')
            else:
                fh.write('<tr>\n')
            fh.write('<td class="table-teamname">\n')
            fh.write('<p><span class="flag-icon flag-icon-' + self.getCountryCode(i) +'"></span><span>' + self.getCountry(i) + '</span></p>\n')
            fh.write('</td>\n')
            fh.write('<td class="table-win"><span class="eng">' + self.getW(i) + '</span></td>\n')
            fh.write('<td class="table-draw"><span class="eng">' + self.getD(i) + '</span></td>\n')
            fh.write('<td class="table-lost"><span class="eng">' + self.getL(i) + '</span></td>\n')
            fh.write('<td class="table-pts"><span class="eng">' + self.getPTS(i) + '</span></td>\n')
            fh.write('</tr>\n')
        fh.write('</tbody>\n')
        fh.write('</table>\n')
        fh.write('</div>\n')
        fh.write('</div>\n')
        fh.write('<!--@2_SPORTS_LIST_' + datetime_now + '(end)@-->\n')
    def print_scoreboard(self):
        print("{}: {}".format(self.group, self.scoreboard))

page = requests.get('http://www.fifa.com/worldcup/groups/')
soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find_all('table')
w, h =4, 8

f_code_A = ['ru', 'uy', 'eg', 'sa']
f_code_B = ['pt', 'es', 'ma', 'ir']
f_code_C = ['fr', 'au', 'pe', 'dk']
f_code_D = ['ar', 'is', 'hr', 'ng']
f_code_E = ['br', 'ch', 'cr', 'rs']
f_code_F = ['de', 'mx', 'se', 'kr']
f_code_G = ['be', 'pa', 'tn', 'gb-eng']
f_code_H = ['pl', 'sn', 'co', 'jp']
groupA = Group(table[0], 'A')
groupB = Group(table[1], 'B')
groupC = Group(table[2], 'C')
groupD = Group(table[3], 'D')
groupE = Group(table[4], 'E')
groupF = Group(table[5], 'F')
groupG = Group(table[6], 'G')
groupH = Group(table[7], 'H')
groupA.print_scoreboard()
groupB.print_scoreboard()
groupC.print_scoreboard()
groupD.print_scoreboard()
groupE.print_scoreboard()
groupF.print_scoreboard()
groupG.print_scoreboard()
groupH.print_scoreboard()

groupA.writeHTML()
groupB.writeHTML()
groupC.writeHTML()
groupD.writeHTML()
groupE.writeHTML()
groupF.writeHTML()
groupG.writeHTML()
groupH.writeHTML()
