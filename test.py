from text_analyzer import farsi_analyzer
import time

main_signal = 'ویرایش و بازخوانی متون فارسی یا به زبان ساده‌تر ویرایش فنی متن‌های فارسی از نظر علائم نگارشی، نکات دستوری و جمله‌بندی، یکی از مهم‌ترین مسائلی است که بیشتر محققان، نام نویسنده‌ها و دانشجویان با آن درگیر هستند. شبکه مترجمین ایران با همکاری و همراهی موسسه (ویراستاران) راه‌حلی مناسب برای آن پیدا کرده است تا دیگر هیچ‌کس نگرانی در مورد ویراستاری متن‌های خود نداشته باشد.'
list_of_words = ['سلام. احوال', 'به نام ', 'مترجمین موسسه', 'خداوند الموت', 'راه‌حل مناسب']
farsi_analyzer = farsi_analyzer()
start = time.time()
print(farsi_analyzer.find_statement(main_passage= main_signal, list_of_statements= list_of_words))
end = time.time()
list_of_words1 = farsi_analyzer.add_statement(list_of_statements=list_of_words, new_statement='تو گاوی')
print(end - start)
