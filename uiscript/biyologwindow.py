import uiScriptLocale
import item
import gameInfo

ROOT = "d:/ymir work/ui/game/"
YOL = str(gameInfo.CONFIG_YOL)+"biyolog/"

WIDTH = 574
HEIGHT = 460

GOREV_X = 7
GOREV_X_EK = 117
GOREV_Y = 74
GOREV_Y_EK = 123

window = {
	"name" : "BiyologWindow","type": "window", "x" : 0,"y" : 0,"style" : ("movable", "float",),"width" : WIDTH,"height" : HEIGHT, "children" :
	(
		
		
		{"name" : "board","type" : "image","x" : 0,"y" : 0,"image": YOL+"arka.tga", "children" :
			(
				## Title
				{"name" : "TitleBar","type" : "titlebar","style" : ("attach",),"x" : 6,"y" : 8,"width" : WIDTH - 16,"color" : "yellow","children" :
					({ "name":"TitleName", "type":"text", "x":0, "y":3, "text":"Biyolog Penceresi", "text_horizontal_align":"center", "horizontal_align": "center" },),
				},
				
				## Animage
				{ "name" : "Animage", "type" : "ani_image", "x" : 7, "y" : 316, "delay" : 4,
				
					"images" : ( 
						YOL+"loading1.tga", 
						YOL+"loading2.tga", 
						YOL+"loading3.tga", 
						YOL+"loading4.tga", 
						YOL+"loading5.tga", 
						YOL+"loading6.tga", 
					),
				
				},
				
				## Görev Butonlarý
				{"name": "gorev30Button", "type": "button", "x":GOREV_X, "y":GOREV_Y, "default_image": YOL+"gelecek.tga", "over_image": YOL+"gelecek1.tga", "down_image": YOL+"gelecek2.tga"},
				{"name": "gorev40Button", "type": "button", "x":GOREV_X+GOREV_X_EK, "y":GOREV_Y, "default_image": YOL+"gelecek.tga", "over_image": YOL+"gelecek1.tga", "down_image": YOL+"gelecek2.tga"},
				{"name": "gorev50Button", "type": "button", "x":GOREV_X+GOREV_X_EK*2, "y":GOREV_Y, "default_image": YOL+"gelecek.tga", "over_image": YOL+"gelecek1.tga", "down_image": YOL+"gelecek2.tga"},
				{"name": "gorev60Button", "type": "button", "x":GOREV_X+GOREV_X_EK*3, "y":GOREV_Y, "default_image": YOL+"gelecek.tga", "over_image": YOL+"gelecek1.tga", "down_image": YOL+"gelecek2.tga"},
				{"name": "gorev70Button", "type": "button", "x":GOREV_X+GOREV_X_EK*4, "y":GOREV_Y, "default_image": YOL+"gelecek.tga", "over_image": YOL+"gelecek1.tga", "down_image": YOL+"gelecek2.tga"},
				{"name": "gorev80Button", "type": "button", "x":GOREV_X, "y":GOREV_Y+GOREV_Y_EK, "default_image": YOL+"gelecek.tga", "over_image": YOL+"gelecek1.tga", "down_image": YOL+"gelecek2.tga"},
				{"name": "gorev85Button", "type": "button", "x":GOREV_X+GOREV_X_EK, "y":GOREV_Y+GOREV_Y_EK, "default_image": YOL+"gelecek.tga", "over_image": YOL+"gelecek1.tga", "down_image": YOL+"gelecek2.tga"},
				{"name": "gorev90Button", "type": "button", "x":GOREV_X+GOREV_X_EK*2, "y":GOREV_Y+GOREV_Y_EK, "default_image": YOL+"gelecek.tga", "over_image": YOL+"gelecek1.tga", "down_image": YOL+"gelecek2.tga"},
				{"name": "gorev92Button", "type": "button", "x":GOREV_X+GOREV_X_EK*3, "y":GOREV_Y+GOREV_Y_EK, "default_image": YOL+"gelecek.tga", "over_image": YOL+"gelecek1.tga", "down_image": YOL+"gelecek2.tga"},
				{"name": "gorev94Button", "type": "button", "x":GOREV_X+GOREV_X_EK*4, "y":GOREV_Y+GOREV_Y_EK, "default_image": YOL+"gelecek.tga", "over_image": YOL+"gelecek1.tga", "down_image": YOL+"gelecek2.tga"},
				
				## Görev Ýstatistikleri
				{"name": "gorevAdiArka","type":"window","x":71,"y":355,"width":122,"height":14, "children": 
					(
						{"name": "gorevAdi", "type": "text", "text": "", "x":0,"y":0, "all_align":"center"},
					),	
				},
				
				{"name": "gorevVerdiginArka","type":"window","x":71,"y":355+22,"width":122,"height":14, "children": 
					(
						{"name": "gorevVerdigin", "type": "text", "text": "", "x":0,"y":0, "all_align":"center"},
					),	
				},
				
				{"name": "gorevKalanArka","type":"window","x":71,"y":355+21*2,"width":122,"height":14, "children": 
					(
						{"name": "gorevKalan", "type": "text", "text": "", "x":0,"y":0, "all_align":"center"},
					),	
				},
				
				{"name": "gorevGelecekArka","type":"window","x":71,"y":355+19*3+10,"width":122,"height":14, "children": 
					(
						{"name": "gorevGelecek", "type": "text", "text": "", "x":0,"y":0, "all_align":"center"},
					),	
				},
				
				## Görev Ýtemler
				{"name": "GorevVereceginItem1", "type":"image", "x":218, "y":359, "image":"icon/item/30515.tga"},
				{"name": "GorevVereceginItem2", "type":"image", "x":219, "y":403, "image":"icon/item/30515.tga"},
				
				{"name": "GorevKazancItem1", "type":"image", "x":281, "y":378, "image":"icon/item/30515.tga"},
				
				## Görev Kazancý
				{"name": "gorevKazanc1Arka","type":"window","x":313,"y":363,"width":122,"height":14, "children": 
					(
						{"name": "gorevKazanc1", "type": "text", "text": "", "x":0,"y":0, "all_align":"center"},
					),	
				},
				
				{"name": "gorevKazanc2Arka","type":"window","x":313,"y":386,"width":122,"height":14, "children": 
					(
						{"name": "gorevKazanc2", "type": "text", "text": "", "x":0,"y":0, "all_align":"center"},
					),	
				},
				
				{"name": "gorevKazanc3Arka","type":"window","x":313,"y":411,"width":122,"height":14, "children": 
					(
						{"name": "gorevKazanc3", "type": "text", "text": "", "x":0,"y":0, "all_align":"center"},
					),	
				},
				
				## Görev Baþlat, Teslim Et
				{"name": "gorevBaslat", "type": "button", "x":451, "y":344, "default_image": YOL+"baslat.tga", "over_image": YOL+"baslat1.tga", "down_image": YOL+"baslat2.tga"},
				{"name": "gorevTeslimEt", "type": "button", "x":451, "y":344, "default_image": YOL+"teslimet.tga", "over_image": YOL+"teslimet1.tga", "down_image": YOL+"teslimet2.tga"},
				
				{"name": "item1Tamamlandi", "type": "image", "x":215, "y":359, "image":str(gameInfo.CONFIG_YOL)+"yenislot_1.tga"},
				{"name": "item2Tamamlandi", "type": "image", "x":215, "y":402, "image":str(gameInfo.CONFIG_YOL)+"yenislot_1.tga"},
			),
		},
	),
}