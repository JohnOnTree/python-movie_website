# coding=utf-8
import media
import fresh_tomatoes

# 封面请求头
head_img_url = "https://i.ytimg.com/an_webp/"
# 预告片请求头
head_vedio_url = "https://youtu.be/"
# 预告片名称数组
movies_names = [ "寻秦记","正義聯盟","武动乾坤", "變形金剛5","妖猫传","星際大戰8"]
# 预告片简介数组
movies_descriptions = ["新版《寻秦记》预告片燃炸来袭【陈翔、郭晓婷、牛子藩、夏楠】",
                       "【正義聯盟】2017國際動漫展預告片《CC中文字幕》",
                        "电视剧《武动乾坤》超燃版决战预告片 Yang Yang TV Drama “Martial Universe” New Trailer",
                        "【變形金剛5：最終騎士】預告片3《中文字幕》",
                        "《妖猫传》Legend of the Demon Cat ‖“探奇”版预告片",
                        "【星際大戰8:最後的絕地武士】HD中文正式電影預告片大首播"]
# 预告片封面数组
movies_imgs = [head_img_url+"7O_dHYVAbHM/mqdefault_6s.webp?du=3000&sqp=CK7T0NAF&rs=AOn4CLCSRHvAq7a2Bcdo9TZRASFz6NyE9w",
                head_img_url+"-FLg7UrMt-Y/mqdefault_6s.webp?du=3000&sqp=CPyh0NAF&rs=AOn4CLB0Pa7pl1PNoip9-xqKDFfkP5-WCA",
                head_img_url+"st6xVqSZPeg/mqdefault_6s.webp?du=3000&sqp=CIDS0NAF&rs=AOn4CLBbw44NMYtejsZpAVT8dLzxpqg7iw",
                head_img_url+"XZfK9ZhSSvo/mqdefault_6s.webp?du=3000&sqp=CJTI0NAF&rs=AOn4CLCNURMV6GCg2wsG_htGOXCUIGUerQ",
                head_img_url+"pAHXil5VU6o/mqdefault_6s.webp?du=3000&sqp=CMi40NAF&rs=AOn4CLDk16REGK6WbJb-Noy4aGyLmhDzDA",
                head_img_url+"kx-4PHuDGko/mqdefault_6s.webp?du=3000&sqp=CLK90NAF&rs=AOn4CLBxzqzhuqPeKqAkqCIRA8zscFXKsA" ]
# 预告片
movies_vedios = [head_vedio_url+"OjL-tHtuZ4g",
                 head_vedio_url+"6tJbPVgZLwA",
                 head_vedio_url+"st6xVqSZPeg",
                 head_vedio_url+"TogrG-UZxWE",
                 head_vedio_url+"G5Hl-o4wMxY",
                 head_vedio_url+"Mnr-Sm2tr6c"]
# 预告片对象
movies = [media.Movie(movies_names[index],movies_descriptions[index],movies_imgs[index],movies_vedios[index]) for index in range(len(movies_names))]
# for index in range(6):
#      movies[index] =  media.Movie(movies_names[index],movies_descriptions[index],movies_imgs[index],movies_vedios[index])

# yldj = media.Movie(
#     "寻秦记","新版《寻秦记》预告片燃炸来袭【陈翔、郭晓婷、牛子藩、夏楠】",
#     head_img_url+"7O_dHYVAbHM/mqdefault_6s.webp?du=3000&sqp=CK7T0NAF&rs=AOn4CLCSRHvAq7a2Bcdo9TZRASFz6NyE9w",head_vedio_url+"OjL-tHtuZ4g")

# rxrq = media.Movie(
#     "正義聯盟","【正義聯盟】2017國際動漫展預告片《CC中文字幕》",
#     head_img_url+"-FLg7UrMt-Y/mqdefault_6s.webp?du=3000&sqp=CPyh0NAF&rs=AOn4CLB0Pa7pl1PNoip9-xqKDFfkP5-WCA",head_vedio_url+"6tJbPVgZLwA")

# yyss = media.Movie(
#     "武动乾坤","电视剧《武动乾坤》超燃版决战预告片 Yang Yang TV Drama “Martial Universe” New Trailer",
#     head_img_url+"st6xVqSZPeg/mqdefault_6s.webp?du=3000&sqp=CIDS0NAF&rs=AOn4CLBbw44NMYtejsZpAVT8dLzxpqg7iw",head_vedio_url+"st6xVqSZPeg")

# xqdz = media.Movie(
#     "變形金剛5","【變形金剛5：最終騎士】預告片3《中文字幕》",
#     head_img_url+"XZfK9ZhSSvo/mqdefault_6s.webp?du=3000&sqp=CJTI0NAF&rs=AOn4CLCNURMV6GCg2wsG_htGOXCUIGUerQ",head_vedio_url+"TogrG-UZxWE")

# pdux = media.Movie(
#     "妖猫传","《妖猫传》Legend of the Demon Cat ‖“探奇”版预告片",
#     head_img_url+"pAHXil5VU6o/mqdefault_6s.webp?du=3000&sqp=CMi40NAF&rs=AOn4CLDk16REGK6WbJb-Noy4aGyLmhDzDA",head_vedio_url+"G5Hl-o4wMxY")

# zshh = media.Movie(
#     "星際大戰8","【星際大戰8:最後的絕地武士】HD中文正式電影預告片大首播",
#     head_img_url+"kx-4PHuDGko/mqdefault_6s.webp?du=3000&sqp=CLK90NAF&rs=AOn4CLBxzqzhuqPeKqAkqCIRA8zscFXKsA",head_vedio_url+"Mnr-Sm2tr6c")


# movies = [yldj,rxrq,yyss,xqdz,pdux,zshh]

# 展示电影网站
fresh_tomatoes.open_movies_page(movies)
