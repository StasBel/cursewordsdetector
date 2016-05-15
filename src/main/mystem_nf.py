from time import time
from pymystem3 import Mystem

mystem = Mystem()


# TODO add mystem

def normal_form1(word):
    return mystem.lemmatize(word.lower())


if __name__ == '__main__':
    before_time = time()
    text = 'Так вот. У меня, как у любого другого человека с двумя маленькими детьми, женой и работой, имеющей девизом классическое «Понедельник начинается в субботу», практически не остается времени на то, чтобы читать что-то в интернете. Панель быстрого доступа в Firefox не даст соврать: «реддит» (несколько раз в день – ветки, посвященные NFL и «Миннесоте»), (пару раз в течение дня – ответы на комментарии в моем блоге, плюс лента подписки), NFL.com (раздел «Fantasy» вечером в четверг – мы с женой соревнуемся, кто из нас худший прогнозист результатов матчей). Последней спортивной «закладкой» до недавнего времени был Grantland.com. Я начал читать «Грантланд» с того момента, когда Билл Симмонс объявил в твиттере «Мы открываемся!» (тогда, четыре года назад, у меня еще было время на ленту твиттера). В число постоянно посещаемых сайтов «Грантланд» попал, когда я сказал себе, что я не хочу знать мнение нескольких футбольных аналитиков; мне хватит одного, пишущего наименее банальные вещи. Выбор пал на Билла Барнуэлла с «Грантланда». В конечном итоге, «Грантланд» остался единственным спортивным сайтом, на котором я мог провести время просто кликая по ссылкам и читая случайные материалы. Но если вы сейчас наберете в браузере grantland.com, то вы увидите то же, что и я неделю с небольшим назад: «Это было отличное время. Спасибо за то, что вы были с нами эти четыре года».'
    print(''.join(mystem.lemmatize(text)))
    now_time = time()
    print(now_time - before_time)