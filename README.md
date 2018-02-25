![KeikyuInfoOnEPaper](https://lh3.googleusercontent.com/khSiS-OUWdNGUPznID1HVxzsq-nzZv0kRztvCCfU9UUB-wbMKRvT6SsXnkAflgzv_3df1hjQfyHASWcP7n7nY1i1OXuKiG_ppBOtMhvx4LLPpCREyI4-cXyXNN6dnumR24qPg7Mfy3M=s600 "KeikyuInfoOnEPaper")


# KeikyuInfoOnEPaper
京急の運行情報をWaveshareの電子ペーパーに表示するスクリプトです


## 概要
[Waveshare](https://www.waveshare.com/)の[2.13inch e-Paper HAT (B)](https://www.waveshare.com/product/modules/oleds-lcds/e-paper/2.13inch-e-paper-hat-b.htm) に、[京急の運行情報](http://unkou.keikyu.co.jp/)を取得し表示するPyhtonスクリプトです。


## 詳細


### [KeikyuPython](https://github.com/pokiiio/KeikyuPython) （keikyu.py）

以前作成した、[京急の運行情報](http://unkou.keikyu.co.jp/)を取得するPythonスクリプトです。コードはこちらで公開しています。

 - https://github.com/pokiiio/KeikyuPython


### [M+ FONTS](https://mplus-fonts.osdn.jp/) （mplus-2p-heavy.ttf）

運行情報の文字列を画像化するのに、PythonのPILを使っていますが、フォントは再配布可能で美しいM+ FONTSを使わせていただきました。ありがとうございました。


### 画像を電子ペーパーに表示する （epd2in13b.py、epdif.py）

この部分のコードは、[Waveshareのサンプルコード](https://www.waveshare.com/wiki/File:2.13inch-e-paper-hat-b-code.7z)に含まれるライブラリを使っています。


## 実際の様子


こんな感じです。


![KeikyuInfoOnEPaper](https://lh3.googleusercontent.com/fcf0nkKXul13phElocjmmuqe8Ypgk1BecJwoIzqXcdmH7qxZYYND9a1fcgftBdIYLuOqCYDuhF-RMql8uCrBVgZOeiLX9iqmlsfghKSSJD_85Gsn4X9pTOvzvi8AnzA_rXJLOeU-_7I=s600 "KeikyuInfoOnEPaper")