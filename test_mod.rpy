init:
    $ mods["test_mod"]=u"Ну допустим тестовый мод"

    # Лэйбл, он же и есть раздел

label test_mod: 

    # Тут заметки решил упустить

    "Приветствую всех читающих этот текстовый материал, данное произвидение/предложение которое вы видите перед экраном является лишь мыслями автора"
    
    th "Ну вот вы и убедились что автор умеет мыслить"

    mi "Я здесь точно не потому что этот текст писал именно Рома"

    "А сейчас мы проверим как автор умеет оперировать над временами года"

    $ prolog_time()

    "Ничего не изменилось? Логично."

    "База"

    "А если так?"

    $ day_time()

    "Уже лучше, не правда ли?"

    "Так, чего ещё тут есть?"

    $ sunset_time()
    
    "Вечер в хату"

    "Пора скрыватся под покровом ночи"

    $ night_time()

    "Темная ночь, только пули свистят по степи"
    "Только ветер гудит в проводах, тускло звезды мерцают"
    "В темную ночь ты любимая знаю не спишь"
    "И у детской кроватки тайком ты слезу утираешь"

    "Ну хватит уже, хватит."

    window hide

    window show

    # Тут будет много текста

    $ set_mode_nvl()

    "«Появился, значит, в Зоне Черный Сталкер. К лагерю ночью повадился приходить и там сует руку в палатку и говорит:
— (загробным, как у зомби голосом) Водииички попиииить, а если не дашь хлебнуть или наружу полезешь, пришибет!
А раз мужик один решил пошутить: вылез тихо из палатки, надел кожаную перчатку, и полез к соседям в палатку. Полез и попрошайничает жалостно:
— Водииички, водииички попить…
А тут из палатки навстречу высовывается рука и за горло его… Цап! И такой сиплый голосок отзывается тихонько:
— (хриплым недовольным голосом) А тебе моя водичка зачем нужна?!»"

    "Смешно?"

    "Хахахах"
    
    "Хватит."

    nvl clear

    "Ну тут нужно чего-нибудь нацарапать лишь бы не пустое окно было"

    "Прошу обратить ваше внимание"
    nvl hide
    "На картинку которой ещё нету"
    "Пока"
    nvl hide dissolve

    nvl show dissolve

    "Мы познакомились с тобой на дискотеке вроде.
    Я приобнял тебя рукой и ты была не против.
    Я пригласил тебя к себе, совсем тебя не зная.
    И мы поехали ко мне на скоростном трамвае."

    $ set_mode_adv()

    "Вот мы и вернулись"

    "Давайте пожалуй вернёмся к лету"

    $ day_time()

    "Красота"

    "Ну, предлагаю взглянуть на местные красоты"

    scene bg bus_stop

    "Ха-ха, едем в ДУТ"

    show sunsethouse with dissolve

    "Тут крч дохуялиард ефектов отображения картинок, прям как в PowerPoint"

    show mi shy pioneer with dissolve

    mi "А вот и я!"

    th "Не удивительно"

    th "Рофл будет "

    show dv shy pioneer with dissolve

    show dv shy pioneer with dissolve:
        linear 0 xalign 0.8
    show mi shy pioneer with dissolve:
        linear 0 xalign 0.1

    dv "ХУЛИ Я НА МИКУ БЛЯТЬ!?"

    th"Потому что я у мамки прогромист"

    el "Лежать плюс сосать"

    th"пиздец ми ебались с етим 40 минут"

    

    

    