library(arules)
library(arulesViz)
library(devtools)
library(wordcloud2)
library(KoNLP) 
library(wordcloud)
library(igraph)
library(RColorBrewer)
library(stringr) 
library(dplyr)
useSejongDic()


"C:/Program Files (x86)/Java/jre1.8.0_172"
Sys.setenv(JAVA_HOME='C:\\Program Files (x86)\\Java\\jre1.8.0_172')
library(rJava)


#夯牢 颇老 困摹, 颇老疙 汲沥->data.frame栏肺 阂矾咳#
moms <- read.csv("C:/Rdata/咀眉技力/妇胶圈腐 - 咀眉技力 2019-8-19  15矫 7盒 (1481扒).csv",as.is=T)
cook <- read.csv("C:/Rdata/咀眉技力/82cook咀眉技力22扒.csv",as.is=T)
blog <- read.csv("C:/Rdata/咀眉技力/喉肺弊 咀眉技力 996扒 2019-8-20  6矫 37盒.csv",as.is=T)
inst <- read.csv("C:/Rdata/咀眉技力/牢胶鸥_咀眉技力_1000.csv",as.is=T)
#坷幅: 凯狼 俺荐啊 凯狼 捞抚甸焊促 腹嚼聪促 -> 捞芭 哆搁 颇老阑 凯绢辑 CSV (桨钎肺 盒府)肺 历厘


#阿 颇老狼 "Words" 眠免窍咯 窍唱狼 函荐 救俊 持澜#
moms.df <- paste(moms$Contents, moms$Comments)
cook.df <- paste(cook$Contents, cook$Comments)
blog.df <- paste(blog$Contents, blog$Comments)
inst.df <- paste(inst$Contents, inst$Comments)


head(moms.df)
mstr(moms.df)   # chr [1:599]
str(cook.df)   # chr [1:23]
str(blog.df)   # chr [1:174]
str(inst.df)   # chr [1:501]
tail(moms.df)

names(moms.df)

#钦摹扁  
com <- c(moms.df, cook.df, blog.df, inst.df)
length(com)

str(com2)
class(com2)  #matrix


#阂鞘夸茄 巩磊 力芭#
ed.dete<- gsub("[^ 啊-芌]","", com)
head(ed.dete)

#技辆 荤傈 窜绢 眠啊#->盒府登辑绰 救登绰 疙荤甸
mergeUserDic(data.frame(c('级蜡蜡楷力','欺角','固技刚瘤','晨货力芭'), c('ncn')))

#疙荤 眠免
noun.dete <- extractNoun(ed.dete)
head(noun.dete)


#窜绢 沥力# ->昏力客 犬牢 馆汗窍搁辑 单捞磐 沥力
word.unlist<-unlist(noun.dete)  

wordcount<-table(word.unlist)
head(sort(wordcount, decreasing=T),100)

word.unlist <- gsub('^技力$','',word.unlist)
word.unlist <- gsub('^荤侩$','',word.unlist)
word.unlist <- gsub('^茄$','',word.unlist)
word.unlist <- gsub('^咀眉$','',word.unlist)
word.unlist <- gsub('^巴$','',word.unlist)
word.unlist <- gsub('^荐$','',word.unlist)
word.unlist <- gsub('^技殴$','',word.unlist)
word.unlist <- gsub('^弧贰$','',word.unlist)
word.unlist <- gsub('^力前$','',word.unlist)
word.unlist <- gsub('^历$','',word.unlist)
word.unlist <- gsub('^窍霸$','',word.unlist)
word.unlist <- gsub('^酒扁$','',word.unlist)
word.unlist <- gsub('^技殴技力$','',word.unlist)

word.unlist <- gsub('^技殴扁$','',word.unlist)
word.unlist <- gsub('^甸$','',word.unlist)
word.unlist <- gsub('^锅$','',word.unlist)
word.unlist <- gsub('^傈$','',word.unlist)

word.unlist <- gsub('^拱$','',word.unlist)
word.unlist <- gsub('^唱$','',word.unlist)
word.unlist <- gsub('^饶$','',word.unlist)
word.unlist <- gsub('^利$','',word.unlist)
word.unlist <- gsub('^老馆$','',word.unlist)
word.unlist <- gsub('^积阿$','',word.unlist)
word.unlist <- gsub('^力$','',word.unlist)

word.unlist <- gsub('^锭巩$','',word.unlist)
word.unlist <- gsub('^蜡酒$','',word.unlist)
word.unlist <- gsub('^窍扁$','',word.unlist)
word.unlist <- gsub('^快府$','',word.unlist)
word.unlist <- gsub('^秦$','',word.unlist)
word.unlist <- gsub('^秦辑$','',word.unlist)
word.unlist <- gsub('^利$','',word.unlist)
word.unlist <- gsub('^唱$','',word.unlist)
word.unlist <- gsub('^盒$','',word.unlist)

word.unlist <- gsub('^快府$','',word.unlist)
word.unlist <- gsub('^窍扁$','',word.unlist)
word.unlist <- gsub('^秦$','',word.unlist)

word.unlist <- gsub('^锭巩$','',word.unlist)
word.unlist <- gsub('^酒捞$','',word.unlist)
word.unlist <- gsub('^殿$','',word.unlist)
word.unlist <- gsub('^屈$','',word.unlist)
word.unlist <- gsub('^矫飘$','',word.unlist)
word.unlist <- gsub('^墨其$','',word.unlist)
word.unlist <- gsub('^霸矫$','',word.unlist)
word.unlist <- gsub('^老$','',word.unlist)
word.unlist <- gsub('^笼$','',word.unlist)
word.unlist <- gsub('^单$','',word.unlist)
word.unlist <- gsub('^啊瓷$','',word.unlist)

word.unlist <- gsub('^固技$','',word.unlist)
word.unlist <- gsub('^傍瘤$','',word.unlist)
word.unlist <- gsub('^弧贰$','',word.unlist)
word.unlist <- gsub('^痹沥$','',word.unlist)
word.unlist <- gsub('^款康$','',word.unlist)
word.unlist <- gsub('^鞘刀$','',word.unlist)
word.unlist <- gsub('^魄喊$','',word.unlist)
word.unlist <- gsub('^霸矫臂累己$','',word.unlist)
word.unlist <- gsub('^矫$','',word.unlist)
word.unlist <- gsub('^窍唱$','',word.unlist)
word.unlist <- gsub('^沥档$','',word.unlist)
word.unlist <- gsub('^林规$','',word.unlist)
word.unlist <- gsub('^啊瘤$','',word.unlist)
word.unlist <- gsub('^滴$','',word.unlist)
word.unlist <- gsub('^蜡楷$','',word.unlist)
word.unlist <- gsub('^酒捞甸$','',word.unlist)

word.unlist <- gsub('^加$','',word.unlist)
word.unlist <- gsub('^急拱$','',word.unlist)
word.unlist <- gsub('^捞$','',word.unlist)
word.unlist <- gsub('^俺$','',word.unlist)
word.unlist <- gsub('^盔$','',word.unlist)
word.unlist <- gsub('^吝$','',word.unlist)
word.unlist <- gsub('^捞亥飘$','',word.unlist)
------------------------------

word.unlist <- gsub('^渴$','',word.unlist)
word.unlist <- gsub('^眠玫$','',word.unlist)
word.unlist <- gsub('^剧$','',word.unlist)
word.unlist <- gsub('^福林福$','',word.unlist)
word.unlist <- gsub('^啊风$','',word.unlist)
word.unlist <- gsub('^级蜡$','',word.unlist)
word.unlist <- gsub('^救傈$','',word.unlist)


word.unlist <- gsub('^级蜡蜡楷力$','',word.unlist)
word.unlist <- gsub('^玫楷$','',word.unlist)
word.unlist <- gsub('^侩$','',word.unlist)
word.unlist <- gsub('^淀$','',word.unlist)
word.unlist <- gsub('^瘤$','',word.unlist)



word.unlist <- word.unlist[nchar(word.unlist)>0]

wordcount<-table(word.unlist)
head(sort(wordcount, decreasing=T),80)


#wordcloud 父甸扁#
wordcount<-head(sort(wordcount, decreasing=T),80)
palete<-brewer.pal(5,"Set1")
windowsFonts(word_font=windowsFont("讣篮 绊雕"))
wordcloud2(data=wordcount, size=1, col="random-dark", rotateRatio = 0)


#惑困 80扒 txt肺 历厘(唱吝俊 况靛 努扼快靛 荤捞飘俊辑 荤侩窍扁 困秦辑 历厘)
wordcount80<-head(sort(wordcount,decreasing=T),80)
names80<-names(wordcount80)
write(names80,"C:/Rdata/咀眉技力 wc80.txt")

chac = as.character(wordcount80)
write(chrac,"C:/Rdata/咀眉技力 wc80.csv", sep=" ")

