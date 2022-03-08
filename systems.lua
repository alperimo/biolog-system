--[[

TR: Tüm özel sistemler, fonksiyonlar, methodlar, ve yol...
TRL : All Special Systems, funcs, method and the way to...

Geliþtirici : .. Fatihbab34™ ..
Paketler ; LuaToPython, PythonToLua, PythonIslem
Fonksiyonlar ; "split('#blabla#blabla#', '#'), systems.getinput('PythonIslem'), io funcs(open, remove, write, read, readline, readlines), table forms, pc.getqf(), pc.setqf()"

--]]

quest systems begin
	state start begin
	
		function biyolog_verial()
			local bol2 = systems.split(biyolog_sistemi["gorev"..tostring(pc.getqf("biyolog_durum"))], "#")
			if pc.getqf("biyolog_durum") == 92 then
				cmdchat("LuaToPython biyolog_verileri|#"..tostring(pc.getqf("biyolog_durum")).."#"..tostring(pc.getqf("biyolog_durum2")).."#"..bol2[9].."#"..tostring(tonumber(bol2[9])-pc.count_item(tonumber(bol2[3]))).."#"..string.gsub(biyolog_sistemi["gorev"..tostring(pc.getqf("biyolog_durum"))],' ','_'))
			else
				cmdchat("LuaToPython biyolog_verileri|#"..tostring(pc.getqf("biyolog_durum")).."#"..tostring(pc.getqf("biyolog_durum2")).."#"..bol2[9].."x"..bol2[10].."#"..tostring(tonumber(bol2[9])-pc.count_item(tonumber(bol2[3]))).."x"..tostring(tonumber(bol2[10])-pc.count_item(tonumber(bol2[4]))).."#"..string.gsub(biyolog_sistemi["gorev"..tostring(pc.getqf("biyolog_durum"))],' ','_'))
			end
		end
		
		
		function biyolog_verial_gelecek(gelen, gelen2)
			local bol = systems.split(gelen,"#")
			local bol2 = systems.split(biyolog_sistemi["gorev"..bol[2]], "#")
			if tonumber(bol[2]) == 92 then	
				cmdchat("LuaToPython biyolog_verileri_gelecek|#"..bol[2].."#0#"..bol2[9].."#"..bol2[9].."#"..string.gsub(biyolog_sistemi["gorev"..bol[2]],' ','_').."#"..gelen2)
			else
				cmdchat("LuaToPython biyolog_verileri_gelecek|#"..bol[2].."#0#"..bol2[9].."x"..bol2[10].."#"..bol2[9].."x"..bol2[10].."#"..string.gsub(biyolog_sistemi["gorev"..bol[2]],' ','_').."#"..gelen2)
			end
		end
		
		function biyolog_kill(gelen)--0: item1, 1:item2, 2:ikisi için
			local item2_var = 0
			local pencere_yenile = 0
			if pc.getqf("biyolog_durum") == 92 then
				item2_var = 1
			end
			
			local bol = systems.split(biyolog_sistemi["gorev"..tostring(pc.getqf("biyolog_durum")).."_itemdusmeorani"],",")
			local bol2 = systems.split(biyolog_sistemi["gorev"..tostring(pc.getqf("biyolog_durum"))],"#")
			local item1 = number(1,tonumber(bol[1]))
			if item1 <= 1 then
				if not (tonumber(bol2[9])-pc.count_item(tonumber(bol2[3])) <= 0) then
					if gelen == 0 or gelen == 2 then
						pc.give_item2_select(tonumber(bol2[3]),1)
						if tonumber(bol2[9])-pc.count_item(tonumber(bol2[3])) > 0 then
							syschat("<Biyolog>: Kalan "..item.get_name().. ": "..tonumber(bol2[9])-pc.count_item(tonumber(bol2[3])))
							
						else
							if tonumber(bol2[9])-pc.count_item(tonumber(bol2[3])) == 0 then
								syschat("<Biyolog>: Yeteri kadar "..item.get_name().. " topladýn.")
					
							end
							--cmdchat("LuaToPython biyolog_itemtoplandi#1")
						end
						pencere_yenile = 1
					end
				end
			end
			if item2_var == 0 then
				if gelen == 1 or gelen == 2 then
					local item2 = number(1, tonumber(bol[2]))
					if item2 <= 2 then
						if not (tonumber(bol2[10])-pc.count_item(tonumber(bol2[4])) <= 0) then
							pc.give_item2_select(tonumber(bol2[4]), 1)
							if tonumber(bol2[10])-pc.count_item(tonumber(bol2[4])) > 0 then
								syschat("<Biyolog>: Kalan "..item.get_name().. ": "..tonumber(bol2[10])-pc.count_item(tonumber(bol2[4])))
							else
								if tonumber(bol2[10])-pc.count_item(tonumber(bol2[4])) == 0 then
									syschat("<Biyolog>: Yeteri kadar "..item.get_name().. " topladýn.")	
								end
							end
							pencere_yenile = 1
						end
					end
				end
			end
			
			if pencere_yenile == 1 then
				--cmdchat("LuaToPython biyolog_yenile#")
				systems.biyolog_verial()
			end
		end
		
		when kill begin
		
			if pc.getqf("biyolog_durum") != 0 and pc.getqf("biyolog_durum2") == 1 then
				
				local biyolog1 = 0
				for i=1, table.getn(biyolog_sistemi["gorev"..tostring(pc.getqf("biyolog_durum")).."_mob"]) do
					if biyolog_sistemi["gorev"..tostring(pc.getqf("biyolog_durum")).."_mob"][i] == npc.get_race() then
						if biyolog1 == 0 then
							biyolog1 = 1
						end
						
					end
				end
				
				local biyolog2 = 0
				for i2=1, table.getn(biyolog_sistemi["gorev"..tostring(pc.getqf("biyolog_durum")).."_mob_2"]) do
					if biyolog_sistemi["gorev"..tostring(pc.getqf("biyolog_durum")).."_mob_2"][i2] == npc.get_race() then
						if biyolog2 == 0 then 
							biyolog2 = 1
						end
					end
				end
				
				if biyolog1 == 1 and biyolog2 == 1 then
					systems.biyolog_kill(2)
				elseif biyolog1 == 1 and biyolog2 == 0 then
					systems.biyolog_kill(0)
				elseif biyolog1 == 0 and biyolog2 == 1 then
					systems.biyolog_kill(1)
				end
			end
		end
		
		when levelup begin
			if pc.get_level() == 30 and pc.getqf("biyolog_durum") == 0 then
				syschat("<Biyolog>: Biyolog görevlerine baþlama vaktin geldi! Baþlamak için sað alttan biyolog butonunu kullan.")
				cmdchat("LuaToPython biyolog_open#")
				pc.setqf("biyolog_durum", 30)
				pc.setqf("biyolog_durum2", 0)
			end
			
		end
		
		when login begin
			cmdchat("PythonToLua "..q.getcurrentquestindex())
			
			if pc.getqf("biyolog_durum") != 0 then
				cmdchat("LuaToPython biyolog_open#")
			end
			
		end

		when button begin
			local gelen = systems.getinput("PYTHONISLEM")
			
			if string.find(gelen, "biyolog_baslat#") then
				bol = systems.split(gelen,"#")
				if pc.getqf("biyolog_durum") == tonumber(bol[2]) and pc.getqf("biyolog_durum2") == 0 and pc.get_level() >= pc.getqf("biyolog_durum") then
					pc.setqf("biyolog_durum2", 1)
					systems.biyolog_verial()
				end
			end
			
			if string.find(gelen,"biyolog_teslimet#") then
				local bol = systems.split(biyolog_sistemi["gorev"..tostring(pc.getqf("biyolog_durum"))], "#")
				local bol2 = systems.split(gelen,"#")
				
				if tonumber(bol[9])-pc.count_item(tonumber(bol[3])) <= 0 and tonumber(bol[10])-pc.count_item(tonumber(bol[4])) <= 0 then
					pc.remove_item(tonumber(bol[3]), tonumber(bol[9]))
					pc.remove_item(tonumber(bol[4]), tonumber(bol[10]))
					pc.give_item2(tonumber(bol[5]))
					local biyolog_durum = pc.getqf("biyolog_durum")
					local biyolog_durum_yeni = 0
					local biyolog_son = 0
					local biyolog_ozellik = 0
					
					if biyolog_durum == 30 then
						affect.add_collect(apply.MOV_SPEED, 10, 60*60*24*365*60)
					elseif biyolog_durum == 40 then
						affect.add_collect(apply.ATT_SPEED, 5, 60*60*24*365*60)
					elseif biyolog_durum == 50 then
						affect.add_collect(apply.DEF_GRADE_BONUS, 60, 60*60*24*365*60)
					elseif biyolog_durum == 60 then
						affect.add_collect(apply.ATT_GRADE_BONUS, 50, 60*60*24*365*60)
					elseif biyolog_durum == 70 then
						affect.remove_collect(apply.MOV_SPEED, 10, 60*60*24*365*60)
						affect.add_collect(apply.MOV_SPEED,21,60*60*24*365*60)	
						affect.add_collect_point(POINT_DEF_BONUS,10,60*60*24*365*60)
					elseif biyolog_durum == 80 then
						affect.remove_collect(apply.ATT_SPEED, 5, 60*60*24*365*60)
                        affect.add_collect(apply.ATT_SPEED,11,60*60*24*365*60)
						affect.add_collect_point(POINT_ATT_BONUS,10,60*60*24*365*60)
					elseif biyolog_durum == 85 then
						affect.add_collect_point(POINT_RESIST_WARRIOR,10,60*60*24*365*60)	
						affect.add_collect_point(POINT_RESIST_ASSASSIN,10,60*60*24*365*60)	
						affect.add_collect_point(POINT_RESIST_SURA,10,60*60*24*365*60)	
						affect.add_collect_point(POINT_RESIST_SHAMAN,10,60*60*24*365*60)	
					elseif biyolog_durum == 90 then
						affect.add_collect_point(POINT_ATTBONUS_WARRIOR,10,60*60*24*365*60)	
						affect.add_collect_point(POINT_ATTBONUS_ASSASSIN,10,60*60*24*365*60)
						affect.add_collect_point(POINT_ATTBONUS_SURA,10,60*60*24*365*60)	
						affect.add_collect_point(POINT_ATTBONUS_SHAMAN,10,60*60*24*365*60)
					elseif biyolog_durum == 92 then
						if tonumber(bol2[3]) == 1 then						
							affect.add_collect(apply.MAX_HP,1000,60*60*24*365*60)
							pc.setqf("biyolog_92hp",1)
						elseif tonumber(bol2[3]) == 2 then							
							affect.add_collect(apply.DEF_GRADE_BONUS,120,60*60*24*365*60)
							pc.setqf("biyolog_92def",1)
						elseif tonumber(bol2[3]) == 3 then							
							affect.remove_collect(apply.ATT_GRADE_BONUS, 50, 60*60*24*365*60)
							pc.setqf("biyolog_92sd",1)
						end 
					elseif biyolog_durum == 94 then
						if tonumber(bol2[3]) == 1 then
							affect.add_collect(apply.MAX_HP,1100,60*60*24*365*60)
							pc.setqf("biyolog_94hp",1)
						elseif tonumber(bol2[3]) == 2 then
							affect.add_collect(apply.DEF_GRADE_BONUS,140,60*60*24*365*60)
							pc.setqf("biyolog_94def",1)	
						elseif tonumber(bol2[3]) == 3 then
							affect.add_collect(apply.ATT_GRADE_BONUS,60,60*60*24*365*60)
							pc.setqf("biyolog_94sd",1)
						end 
					end
					
					if biyolog_durum >= 30 and biyolog_durum <= 70 then
						pc.setqf("biyolog_durum", biyolog_durum+10)
						pc.setqf("biyolog_durum2", 0)
						syschat("<Biyolog>: Tebrikler "..biyolog_durum.. " level biyolog görevini tamamladýn.")
					else
						if biyolog_durum == 80 or biyolog_durum == 85 then
							biyolog_durum_yeni = biyolog_durum+5
						elseif biyolog_durum == 90 or biyolog_durum == 92 then
							biyolog_durum_yeni = biyolog_durum+2
						elseif biyolog_durum == 94 then
							biyolog_son = 1
						end
						
						if biyolog_son == 1 then
							pc.delqf("biyolog_durum")
							pc.delqf("biyolog_durum2")
							cmdchat("LuaToPython biyolog_kapat#")
							return
						else
							syschat("<Biyolog>: Tebrikler "..biyolog_durum.. " level biyolog görevini tamamladýn.")
						end
						
						pc.setqf("biyolog_durum2", 0)
						pc.setqf("biyolog_durum", biyolog_durum_yeni)
					end
					
					systems.biyolog_verial_gelecek("fatihbab34#"..tostring(pc.getqf("biyolog_durum")),"1")
					--cmdchat("LuaToPython biyolog_yenile#2#"..tostring(pc.getqf("biyolog_durum")))
				else
					syschat("<Biyolog>: Görevi tamamlamak için yeterli malzeme yok.")
				end
				
			end
			
			if string.find(gelen, "biyolog_verial#") then
				systems.biyolog_verial()
			end
			
			if string.find(gelen, "biyolog_verial_gelecek#") then
				systems.biyolog_verial_gelecek(gelen,"0")
			end
		end

		function getinput(gelen)
			local input1 = "#quest_input#"
			local input0 = "#quest_inputbitir#"
			cmdchat("LuaToPython "..input1)
			local al = input(cmdchat("PythonIslem "..gelen))
			cmdchat("LuaToPython "..input0)
			return al
		end

		function split(command_, ne)
			return systems.split_(command_,ne)
		end
		
		function split_(string_,delimiter)
			local result = { }
			local from  = 1
			local delim_from, delim_to = string.find( string_, delimiter, from  )
			while delim_from do
				table.insert( result, string.sub( string_, from , delim_from-1 ) )
				from  = delim_to + 1
				delim_from, delim_to = string.find( string_, delimiter, from  )
			end
			table.insert( result, string.sub( string_, from  ) )
			return result
		end

	end
end