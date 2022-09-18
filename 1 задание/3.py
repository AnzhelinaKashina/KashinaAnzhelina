seconds=int(input('введите количество секунд' ))
days=seconds // (3600*24) # в одном часе 60мин *60 секунд =3600 сек ,в сутках 24 часа
hours=seconds// 3600
minutes =seconds//60
sec=seconds //1
print(days,'дней',hours,'часов',minutes ,'минут', sec,"секунд" )