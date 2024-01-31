I have kept the entire project very simple, i.e. I have stuck to the basic operations like: Adding new information, Searching new information, deleting the existing information, Updating the existing information, etc. The information regarding the armed forces is very hard to come by because anything related to the life of soldiers or the defence services is protected by layers and layers of bureaucratic red tape because of national security reasons.
 	I still managed to compile data on different sectors of the defence services like: Soldier Information, What kind of weapons they use, who is manufacturing those weapons, What all categories do these weapons fall under, What battalion does a particular soldier belong to, what are the different medals that are awarded in the defence services, are there any active wars, what is the status of the soldier, where is he/she posted and location, 
	The problem that I encountered was the frontend part, due to my limited knowledge of python I was able to create a display only for limited amount of information, so I have implemented the program to display the Soldier Information but to display other information we have to make the necessary changes in both the front end and backend.

Entity Data
Some of the major tables I have displayed below:
1.	Soldier:
 

2.	Manufacturing Details:
 

3.	Category:
 

4.	Weapons:
 

5.	Battalion:
 
6.	Medal:
 

7.	Company:
 






ER DIAGARAM
 

RELATIONAL SCHEMA:
 

Tables (SQL)
Soldier
SET SEARCH_PATH TO armydb;

  INSERT INTO "soldier" (ID, name, rank, doj, dob,dor,b_name,birthplacepincode,sex,height, weight, chest, Sex) 
  VALUES (44668,'Kamal Awasthi','Soldier','2013-02-12','1993-04-21','2043-02-23','Madras Regiment',382421,1,162,65,40);

INSERT INTO soldier VALUES(19339,'Arjun Pratap','Soldier','2012-4-15','1987-5-23','2059-8-20','Sikh Regiment',382436,1,176,70,40);
INSERT INTO soldier VALUES(33998,'Karan Jagtap','Soldier','2008-5-16','1982-5-23','2049-4-21','Sikh Regiment',382427,1,179,76,39);
INSERT INTO soldier VALUES(13423,'Jaspreet Singh Kaur','Soldier','2010-9-24','1985-9-9','2054-4-17','Sikh Regiment',382426,1,182,75,40);
INSERT INTO soldier VALUES(49159,'Vijay Kumar Ahirwar','Major General','2011-3-15','1983-4-27','2020-3-21','Sikh Regiment',382427,1,176,70,40);
INSERT INTO soldier VALUES (29603,'Rohan Dhoot','Soldier','2005-6-21','1987-8-24','2012-5-17','Sikh Soldier',382429,1,182,76,37);
INSERT INTO soldier VALUES (21474,'Brijmohan Singh','Field Marshal','2010-12-21','1990-12-24','2050-5-17','Sikh Regiment',382422,1,172,80,41);
INSERT INTO soldier VALUES(12498,'Rajat Talesra','Soldier','2008-12-4','1995-01-13','2048-12-10','Sikh Regiment',382425,1,177,79,43);
INSERT INTO soldier VALUES(14298,'Niranjan Arya','Lieutenant General','2014-5-14','1996-11-12','2054-02-01','Sikh Regiment',382421,1,158,82,43);
INSERT INTO soldier VALUES (10923,'Disha Singh','Major General','2001-05-25','1990-10-2','2041-02-01','Jat Regiment',382424,1,171,52,42);
INSERT INTO soldier Values(12398,'Saurabh Pandit','Soldier','2011-4-15','1996-03-29','2051-12-11','Jat Regiment',382423,1,185,74,42);
INSERT INTO soldier VALUES(12245,'Dheeru','Soldier','2010-9-11','1990-02-24','2040-06-16', 'Jat Regiment',382425,1,172,78,43);
INSERT INTO soldier VALUES (10305,'Vikul Kumar','Captain','2014-10-11','1994-01-24','2050-07-16','Jat Regiment',382426,1,176,75,41);
INSERT INTO soldier VALUES (12051,'Mayank','Soldier','2011-9-21','1991-02-24','2045-06-26','Jat Regiment',382427,1,174,75,42);
INSERT INTO soldier VALUES (12300,'Piyush', 'Soldier', '2005-9-21','1985-01-24','2040-06-16','Madras Regiment', 382428, 1,162,68,41);
INSERT INTO soldier VALUES (12105,'Yogendra','Major','2009-6-11','1989-02-14','2042-07-26','Jat Regiment',382429,1,162,68,41);
INSERT INTO soldier VALUES (14345,'Shubham verma','Soldier','2004-3-11','1990-02-24','2040-05-26','Jat Regiment',282429,1,172,78,42);
INSERT INTO soldier VALUES (11145,'Ankur Ranjan','Brigadier','2013-10-11','1990-01-14','2050-07-16','Sikh Regiment',382430,1,170,76,43);
INSERT INTO soldier VALUES (12115,'Anil Kumvat','Soldier','2008-10-11','1988-06-14','2045-07-16','Madras Regiment',382431,1,171,80,42);
INSERT INTO soldier VALUES (12045,'Himanshu Kumar','Soldier','2011-8-11','1990-03-16','2052-07-16','Madras Regiment',382432,1,172,80,41);
INSERT INTO soldier VALUES(10345,'Vikram Meena','Lieutenant','2013-6-18','1992-08-28','2055-09-16','Rajputana Rifles',382433,1,176,88,40);
INSERT INTO soldier VALUES (10045,'Shubhandra Vikram','Soldier','2007-10-19','1987-03-11','2045-08-26','Rajputana Rifles', 382434, 1, 173,74,42);
INSERT INTO soldier VALUES (12005,'Vikas Singh','Colonel','2015-10-21','1994-07-14','2055-04-26','Rajput Regiment',382436,1,174,81,40);
INSERT INTO soldier VALUES (11305,'Rohit Singh','Havildar','2011-1-21','1989-09-14','2056-06-16','Rajput Regiment',382437,1,173,86,41);
INSERT INTO soldier VALUES (11045,'Shivam Singh','Soldier','2013-8-29','1990-08-14','2050-08-26','Rajputana Riffles',382422,1,177,78,42);
INSERT INTO soldier VALUES (21045,'Shubham Singh','Soldier','2000-11-29','1980-01-24','2045-01-26','Sikh Regiment',382424,1,178,88,41);
INSERT INTO soldier VALUES (21040,'Sunny Prakash','Soldier','2013-1-29','1991-05-14','2047-04-16','Jat Regiment',382425,1,169,74,45);
INSERT INTO soldier VALUES (22045,'Virat Kohli','Major','2011-10-21','1992-06-11','2048-01-26','Madras Regiment',382426,1,175,68,43);
INSERT INTO soldier VALUES (13045,'Ayush Mudgal','Havildar','2010-9-19','1989-01-24','2045-01-20','Madras Regiment',382426,1,172,80,42);
INSERT INTO soldier VALUES (11046,'Kilan Ravani','Soldier','2011-8-30','1990-03-18','2044-04-16','Sikh Regiment',382427,1,175,78,43);
INSERT INTO soldier VALUES(36099,'Rajesh Kumar panth','Havildar','2005-07-02','1985-3-11',,'2040-10-11''Madras Regiment','382422','1',160,64,42);
INSERT INTO soldier VALUES(12345,'Bishan Singh Bedi','Lieutenant','2006-08-09','1987-4-11','2042-10-10','Madras Regiment',382421,1,162,65,41);
INSERT INTO soldier VALUES(17694,'Harminder Kaur','Field Marshal','2005-08-09','1985-5-25','2042-10-11','Madras Regiment',382428,1,160,55,40);
INSERT INTO soldier VALUES(49158,'Satveer Singh Thakur','Major General','2004-10-19','1980-4-20','2040-05-10','Madras Regiment',382426,1,162,54,42);
INSERT INTO soldier VALUES(44668,'Chuni Lal','Soldier','2004-06-12','1982-2-21','2041-06-11','Madras Regiment',382424,1,168,60,52);
INSERT INTO soldier VALUES(26548,'Bijendra Verma','Soldier','2006-08-09','1981-8-12','2045-05-10','Madras Regiment',382423,1,167,59,50);
INSERT INTO soldier VALUES(28613,'Hamid Ahmed Qureshi','Soldier','2008-02-24','1988-6-10','2036-04-02','Madras Regiment',382422,1,164,54,38);
INSERT INTO soldier VALUES(27989,'Rakshit Jain','Major','2013-08-06','1990-2-13','2040-06-12','Madras Regiment',382424,1,169,59,42);
INSERT INTO soldier VALUES(14256,'Subham Singh','Captain','2010-05-04','1988-6-13','2050-02-12','Rajputana Rifles',382430,1,168,54,40);
INSERT INTO soldier VALUES(48563,'Ajay Singh Kumnawat','Colonel','2003-07-08','1984-4-12','2051-02-11','2051-02-11','Rajputana Rifles',382432,1,165,52,40);
INSERT INTO soldier VALUES(33728,'Sandeep Singh','Brigadier','2009-08-18','1983-5-21','2051-5-18','Rajputana Rifles',382424,1,168,58,44);
INSERT INTO soldier VALUES(11053,'Avantika Kulkarni','Soldier','2012-4-26','1990-5-16','2058-6-21','Rajputana Rifles',382425,1,167,56,40);
INSERT INTO soldier VALUES(23432,'Abhishek Saxena','Soldier','2005-5-12','1985-5-16','2049-3-21','Rajputana Rifles',382426,1,176,57,41);
INSERT INTO soldier VALUES(22513,'Rajveer Singh','Captain','2010-2-15','1988-2-15','2054-1-18','Rajputana Rifles',382428,1,175,67,48);
INSERT INTO soldier VALUES(40386,'Vijay Singh Rajput','Soldier','2012-4-19','1989-3-24','2058-3-9','Rajput Regiment',382427,1,176,72,78);
INSERT INTO soldier VALUES(31931,'Satyam Singh Rathore','Soldier','2010-3-17','1986-4-12','2053-3-23','Rajput Regiment',382426,1,172,62,75);
INSERT INTO soldier VALUES(19338,'Arjun Pratap','Soldier','2012-4-15','1987-5-23','2059-8-20','Rajput Regiment',382427,1,176,70,74);
INSERT INTO soldier VALUES(33994,'Karan Jagtap','Soldier','2008-5-16','1982-5-23','2049-4-21','Rajput Regiment',382432,1,179,76,74);
INSERT INTO soldier VALUES(13424,'Jaspreet Singh Kaur','Soldier','2010-9-24','1982-5-23','2050-9-9','Rajput Regiment',382430,0,175,77,74);
INSERT INTO soldier VALUES(49158,'Vijay Kumar Ahirwar','Captain','2011-3-15','1985-9-9','2049-4-21','Rajput Regiment',382434,1,176,78,69);
INSERT INTO soldier VALUES(14245, 'Mikel','Soldier','1996-05-20', '1954-05-05' , '2018-01-04' ,'Rajputana Rifles' , '382436' ,'1', '160' ,'62' ,'42');
INSERT INTO soldier VALUES(14255, 'Rohan Dhoot','Captain','1982-05-20', '1952-06-06' , '2010-02-05' ,'Rajputana Rifles' , '382437' ,'1', '165' , '65' , '40');
INSERT INTO soldier VALUES(14345, 'Mh. Hamid Qureshi','Soldier','2004-02-25', '1984-08-20' , '2030-02-05' ,'Madras Regiment' , '382425' ,'1', '168' , '56' , '42');
INSERT INTO soldier VALUES(48563, 'Ashish','Soldier','1998-02-28', '1983-08-20' , '2032-02-08' ,'Jat Regiment' , '382427' ,'1', '167' , '57' , '41');
INSERT INTO soldier VALUES(36099, 'Ansuman','Soldier','1996-04-18', '1985-08-21' , '2031-12-18' ,'Sikh Regiment' , '382431' ,'1', '167' , '57' , '41');
INSERT INTO soldier Values(11088,'Tony','Soldier','1994-04-05', '1964-06-13' , '2022-06-12' ,'Sikh Regiment' , '382431' ,'1', '167' , '57' , '41');
INSERT INTO soldier VALUES(13043, 'harry','Soldier','1995-05-20', '1955-05-05' , '2020-10-14' ,'Rajputana Rifles' , '382434' ,'1', '164' ,'63' ,'43');

Manufacturing Details
SET SEARCH_PATH TO armydb;
INSERT INTO "manufacturing_details" (weapon_id, manufacturing_date, manufacting_location, company_name) VALUES (1053,'2000-01-1','Argentina','Bersa');
INSERT INTO "manufacturing_details" (weapon_id, manufacturing_date, manufacting_location, company_name) VALUES (1054,'2001-02-2','Australia','Boeing Australia');
INSERT INTO "manufacturing_details" (weapon_id, manufacturing_date, manufacting_location, company_name) VALUES (1055,'2005-03-3','Austria','Steyr Mannlicher');
INSERT INTO "manufacturing_details" (weapon_id, manufacturing_date, manufacting_location, company_name) VALUES (1056,'2002-04-4','Azerbaijan','MDI Azerbaijan');
INSERT INTO "manufacturing_details" (weapon_id, manufacturing_date, manufacting_location, company_name) VALUES (1057,'2003-05-5','Bangladesh','Defence Advancement Trading Company (DATCO)');
INSERT INTO "manufacturing_details" (weapon_id, manufacturing_date, manufacting_location, company_name) VALUES (1058,'2001-06-6','Belgium','Fabrique Nationale de Herstal');
INSERT INTO "manufacturing_details" (weapon_id, manufacturing_date, manufacting_location, company_name) VALUES (1059,'2002-07-7','Bosnia and Herzegovina','Pretis dd');
INSERT INTO "manufacturing_details" (weapon_id, manufacturing_date, manufacting_location, company_name) VALUES (1060,'2006-08-8','Brazil','Avibras');
INSERT INTO "manufacturing_details" (weapon_id, manufacturing_date, manufacting_location, company_name) VALUES (1061,'2005-09-9','Bulgaria','TEREM');
INSERT INTO "manufacturing_details" (weapon_id, manufacturing_date, manufacting_location, company_name) VALUES (1062,'2001-10-10','India','Hindustan Aeronautics Limited');
INSERT INTO "manufacturing_details" (weapon_id, manufacturing_date, manufacting_location, company_name) VALUES (1063,'2000-11-11','Argentina','Bersa');
INSERT INTO "manufacturing_details" (weapon_id, manufacturing_date, manufacting_location, company_name) VALUES (1064,'2003-12-12','Australia','Boeing Australia');
INSERT INTO "manufacturing_details" (weapon_id, manufacturing_date, manufacting_location, company_name) VALUES (1065,'2005-1-13','Austria','Steyr Mannlicher');
INSERT INTO "manufacturing_details" (weapon_id, manufacturing_date, manufacting_location, company_name) VALUES (1066,'2002-2-14','Azerbaijan','MDI Azerbaijan');
INSERT INTO "manufacturing_details" (weapon_id, manufacturing_date, manufacting_location, company_name) VALUES (1067,'2001-3-15','Bangladesh','Defence Advancement Trading Company (DATCO)');
INSERT INTO "manufacturing_details" (weapon_id, manufacturing_date, manufacting_location, company_name) VALUES (1068,'2004-4-16','Belgium','Fabrique Nationale de Herstal');
INSERT INTO "manufacturing_details" (weapon_id, manufacturing_date, manufacting_location, company_name) VALUES (1069,'2003-5-17','Bosnia and Herzegovina','Pretis dd');
INSERT INTO "manufacturing_details" (weapon_id, manufacturing_date, manufacting_location, company_name) VALUES (1070,'2006-6-18','Brazil','Avibras');
INSERT INTO "manufacturing_details" (weapon_id, manufacturing_date, manufacting_location, company_name) VALUES (1071,'2002-7-19','Bulgaria','TEREM');
INSERT INTO "manufacturing_details" (weapon_id, manufacturing_date, manufacting_location, company_name) VALUES (1072,'2000-8-20','India','Hindustan Aeronautics Limited');
INSERT INTO "manufacturing_details" (weapon_id, manufacturing_date, manufacting_location, company_name) VALUES (1073,'2001-9-21','Argentina','Bersa');
INSERT INTO "manufacturing_details" (weapon_id, manufacturing_date, manufacting_location, company_name) VALUES (1074,'2005-10-22','Australia','Boeing Australia');
INSERT INTO "manufacturing_details" (weapon_id, manufacturing_date, manufacting_location, company_name) VALUES (1075,'2004-11-23','Austria','Steyr Mannlicher');
INSERT INTO "manufacturing_details" (weapon_id, manufacturing_date, manufacting_location, company_name) VALUES (1076,'2006-12-24','Azerbaijan','MDI Azerbaijan');
INSERT INTO "manufacturing_details" (weapon_id, manufacturing_date, manufacting_location, company_name) VALUES (1077,'2003-1-25','Bangladesh','Defence Advancement Trading Company (DATCO)');
INSERT INTO "manufacturing_details" (weapon_id, manufacturing_date, manufacting_location, company_name) VALUES (1078,'2004-2-26','Belgium','Fabrique Nationale de Herstal');
INSERT INTO "manufacturing_details" (weapon_id, manufacturing_date, manufacting_location, company_name) VALUES (1079,'2001-3-27','Bosnia and Herzegovina','Pretis dd');
INSERT INTO "manufacturing_details" (weapon_id, manufacturing_date, manufacting_location, company_name) VALUES (1080,'2003-4-28','Brazil','Avibras');
INSERT INTO "manufacturing_details" (weapon_id, manufacturing_date, manufacting_location, company_name) VALUES (1081,'2002-5-1','Bulgaria','TEREM');
INSERT INTO "manufacturing_details" (weapon_id, manufacturing_date, manufacting_location, company_name) VALUES (1082,'2001-6-2','India','Hindustan Aeronautics Limited');
INSERT INTO "manufacturing_details" (weapon_id, manufacturing_date, manufacting_location, company_name) VALUES (1083,'2006-7-3','India','Hindustan Aeronautics Limited');
INSERT INTO "manufacturing_details" (weapon_id, manufacturing_date, manufacting_location, company_name) VALUES (1084,'2003-8-4','India','Hindustan Aeronautics Limited');
INSERT INTO "manufacturing_details" (weapon_id, manufacturing_date, manufacting_location, company_name) VALUES (1085,'2004-9-5','India','Hindustan Aeronautics Limited'); 

Weapons
SET SEARCH_PATH TO armydb;
INSERT INTO "weapons" (weapon_id,name) VALUES (1053, 'Glock-18');
INSERT INTO "weapons" (weapon_id,name) VALUES (1054, 'Dual Berettas');
INSERT INTO "weapons" (weapon_id,name) VALUES (1055, 'P250');
INSERT INTO "weapons" (weapon_id,name) VALUES (1056, 'Tec-9');
INSERT INTO "weapons" (weapon_id,name) VALUES (1057, 'CZ75-Auto');
INSERT INTO "weapons" (weapon_id,name) VALUES (1058, 'Desert Eagle');
INSERT INTO "weapons" (weapon_id,name) VALUES (1059, 'R8 Revolver');
INSERT INTO "weapons" (weapon_id,name) VALUES (1060, 'USP-S');
INSERT INTO "weapons" (weapon_id,name) VALUES (1061, 'P2000');
INSERT INTO "weapons" (weapon_id,name) VALUES (1062, 'Five-Seven');
INSERT INTO "weapons" (weapon_id,name) VALUES (1063, 'Nova');
INSERT INTO "weapons" (weapon_id,name) VALUES (1064, 'XM1014');
INSERT INTO "weapons" (weapon_id,name) VALUES (1065, 'Sawed-Off');
INSERT INTO "weapons" (weapon_id,name) VALUES (1066, 'M249');
INSERT INTO "weapons" (weapon_id,name) VALUES (1067, 'Negev');
INSERT INTO "weapons" (weapon_id,name) VALUES (1068, 'MAG-7');
INSERT INTO "weapons" (weapon_id,name) VALUES (1069, 'MAC-10');
INSERT INTO "weapons" (weapon_id,name) VALUES (1070, 'MP7');
INSERT INTO "weapons" (weapon_id,name) VALUES (1071, 'UMP-45');
INSERT INTO "weapons" (weapon_id,name) VALUES (1072, 'P90');
INSERT INTO "weapons" (weapon_id,name) VALUES (1073, 'PP-Bizon');
INSERT INTO "weapons" (weapon_id,name) VALUES (1074, 'MP9');
INSERT INTO "weapons" (weapon_id,name) VALUES (1075, 'Galil AR');
INSERT INTO "weapons" (weapon_id,name) VALUES (1076,'AK-47');
INSERT INTO "weapons" (weapon_id,name) VALUES (1077, 'SSG 08');
INSERT INTO "weapons" (weapon_id,name) VALUES (1078, 'SG 553');
INSERT INTO "weapons" (weapon_id,name) VALUES (1079, 'AWP');
INSERT INTO "weapons" (weapon_id,name) VALUES (1080, 'G3SG1');
INSERT INTO "weapons" (weapon_id,name) VALUES (1081, 'FAMAS');
INSERT INTO "weapons" (weapon_id,name) VALUES (1082, 'M4A4');
INSERT INTO "weapons" (weapon_id,name) VALUES (1083, 'M4A1-S');
INSERT INTO "weapons" (weapon_id,name) VALUES (1084, 'AUG');
INSERT INTO "weapons" (weapon_id,name) VALUES (1085, 'SCAR-20');

Company
SET SEARCH_PATH TO armydb;
INSERT INTO "company" (company_name, country_name) VALUES ('Bersa', 'Argentina');
INSERT INTO "company" (company_name, country_name) VALUES ('Boeing Australia', 'Australia');
INSERT INTO "company" (company_name, country_name) VALUES ('Steyr Mannlicher', 'Austria');
INSERT INTO "company" (company_name, country_name) VALUES ('MDI Azerbaijan', 'Azerbaijan');
INSERT INTO "company" (company_name, country_name) VALUES ('Defence Advancement Trading Company (DATCO)', 'Bangladesh');
INSERT INTO "company" (company_name, country_name) VALUES ('Fabrique Nationale de Herstal', 'Belgium');
INSERT INTO "company" (company_name, country_name) VALUES ('Pretis dd', 'Bosnia and Herzegovina');
INSERT INTO "company" (company_name, country_name) VALUES ('Avibras', 'Brazil');
INSERT INTO "company" (company_name, country_name) VALUES ('TEREM', 'Bulgaria');
INSERT INTO "company" (company_name, country_name) VALUES ('Hindustan Aeronautics Limited', 'India');
INSERT INTO "company" (company_name, country_name) VALUES ('HMT', 'America');

Category
SET SEARCH_PATH TO armydb;
INSERT INTO "category" (name,class)VALUES('Glock-18','Pistol');
INSERT INTO "category" (name,class)VALUES('Dual Berettas','Pistol');
INSERT INTO "category" (name,class)VALUES('P250','Pistol');
INSERT INTO "category" (name,class)VALUES('Tec-9','Pistol');
INSERT INTO "category" (name,class)VALUES('CZ75-Auto','Pistol');
INSERT INTO "category" (name,class)VALUES('Desert Eagle','Pistol');
INSERT INTO "category" (name,class)VALUES('R8 Revolver','Pistol');
INSERT INTO "category" (name,class)VALUES('USP-S','Pistol');
INSERT INTO "category" (name,class)VALUES('P2000','Pistol');
INSERT INTO "category" (name,class)VALUES('Five-Seven','Pistol');

INSERT INTO "category" (name,class)VALUES('Nova','Heavy');
INSERT INTO "category" (name,class)VALUES('XM1014','Heavy');
INSERT INTO "category" (name,class)VALUES('Sawed-Off','Heavy');
INSERT INTO "category" (name,class)VALUES('M249','Heavy');
INSERT INTO "category" (name,class)VALUES('Negev','Heavy');
INSERT INTO "category" (name,class)VALUES('MAG-7','Heavy');

INSERT INTO "category" (name,class)VALUES('MAC-10','submachine gun');
INSERT INTO "category" (name,class)VALUES('MP7','submachine gun');
INSERT INTO "category" (name,class)VALUES('UMP-45','submachine gun');
INSERT INTO "category" (name,class)VALUES('P90','submachine gun');
INSERT INTO "category" (name,class)VALUES('PP-Bizon','submachine gun');
INSERT INTO "category" (name,class)VALUES('MP9','submachine gun');

INSERT INTO "category" (name,class)VALUES('Galil AR','rifles');
INSERT INTO "category" (name,class)VALUES('AK-47','rifles');
INSERT INTO "category" (name,class)VALUES('SSG 08','rifles');
INSERT INTO "category" (name,class)VALUES('SG 553','rifles');
INSERT INTO "category" (name,class)VALUES('AWP','rifles');
INSERT INTO "category" (name,class)VALUES('G3SG1','rifles');
INSERT INTO "category" (name,class)VALUES('FAMAS','rifles');
INSERT INTO "category" (name,class)VALUES('M4A4','rifles');
INSERT INTO "category" (name,class)VALUES('M4A1-S','rifles');
INSERT INTO "category" (name,class)VALUES('AUG','rifles');
INSERT INTO "category" (name,class)VALUES('SCAR-20 ','rifles');


Battalion
SET SEARCH_PATH to armydb;
INSERT INTO battalian VALUES('Madras Regiment', 13011, 1992,20);
INSERT INTO battalian VALUES('Madras Regiment',27989,2013,25);
INSERT INTO battalian VALUES('Rajputana Rifles' ,14255,1996,18);
INSERT INTO battalian VALUES('Rajputana Rifles' ,14256,2010,22);
INSERT INTO battalian VALUES('Sikh Regiment',12402,1980,15);
INSERT INTO battalian VALUES('Sikh Regiment',11046,2011,19);
INSERT INTO battalian VALUES('Jat Regiment',11238,1994,18);
INSERT INTO battalian VALUES('Jat Regiment',10305,2014,24);
INSERT INTO battalian VALUES('Rajput Regiment',12356,1982,15);
INSERT INTO battalian VALUES('Rajput Regiment',49158,2011,18);

Medal
SET SEARCH_PATH to armydb;
INSERT INTO medal VALUES('Ashok Chakra Award ');
INSERT INTO medal VALUES('Kirti Chakra ');
INSERT INTO medal VALUES('Shaurya Chakra ');
INSERT INTO medal VALUES('Sarvottam Yudh Seva Medal');
INSERT INTO medal VALUES('Yudh Seva Medal');
INSERT INTO medal VALUES('Ati Vishisht Seva Medal ');
INSERT INTO medal VALUES('Vishisht Seva Medal');
INSERT INTO medal VALUES('Bharat Award ');
INSERT INTO medal VALUES('Sarvottam Jeevan Raksha Padak'); 
INSERT INTO medal VALUES('Uttam Jeevan Raksha Padak'); 
INSERT INTO medal VALUES('Jeevan Raksha Padak');

Work
SET SEARCH_PATH TO armydb;
INSERT INTO "work"(type, salary) Values ('Soldier', '23000');
INSERT INTO "work"(type, salary) Values ('Havildar', '12000');
INSERT INTO "work"(type, salary) Values ('Lieutenant', '56100');
INSERT INTO "work"(type, salary) Values ('Field Marshal', '250000');
INSERT INTO "work"(type, salary) Values ('Lieutenant General', '225000');
INSERT INTO "work"(type, salary) Values ('Major General', '144200');
INSERT INTO "work"(type, salary) Values ('Brigadier', '134400');
INSERT INTO "work"(type, salary) Values ('Colonel', '125700');
INSERT INTO "work"(type, salary) Values ('Major', '69400');
INSERT INTO "work"(type, salary) Values ('Captain', '61300');

War
SET SEARCH_PATH TO armydb;
insert into war VALUES(1,382429,'2003-03-17');
Insert into war VALUES(0,382425,'1995-10-01');
Insert into war VALUES(1,382427,'1997-07-25');
Insert into war VALUES(1,382423,'2000-05-13');
Insert into war VALUES(0,382423,'2003-09-29');
Insert into war VALUES(0,382426,'2002-04-10');

Soldier Status
set search_path to armydb;
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(19339,1,'2003-03-17','382429');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(33998,1,'1995-10-01','382425');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(49159,1,'1997-07-25','382427');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(21474,1,'2000-05-13','382423');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(12498,0,'2003-09-29','382423');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(14298,1,'2002-04-10','382426');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(12398,01,'2003-03-17','382429');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(13424,01,'1995-10-01','382425');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(28613,01,'1997-07-25','382427');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(13011,01,'2000-05-13','382423');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(12300,01,'2003-09-29','382423');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(14256,0,'2002-04-10','382426');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(11088,0,'2003-03-17','382429');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(13423,01,'1995-10-01','382425');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(14345,0,'1997-07-25','382427');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(21045,01,'2000-05-13','382423');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(21040,0,'2003-09-29','382423');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(22045,01,'2002-04-10','382426');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(13045,01,'2003-03-17','382429');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(29603,01,'1995-10-01','382425');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(12245,01,'1997-07-25','382427');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(10305,01,'2000-05-13','382423');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(48563,01,'2003-09-29','382423');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(10923,01,'2002-04-10','382426');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(12051,0,'2003-03-17','382429');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(12105,01,'1995-10-01','382425');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(11145,01,'1997-07-25','382427');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(12115,01,'2000-05-13','382423');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(12045,01,'2003-09-29','382423');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(10345,01,'2002-04-10','382426');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(10045,01,'2003-03-17','382429');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(36099,0,'1995-10-01','382425');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(12345,01,'1997-07-25','382427');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(33728,01,'2000-05-13','382423');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(23432,01,'2003-09-29','382423');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(40386,01,'2002-04-10','382426');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(31931,01,'2003-03-17','382429');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(19338,01,'1995-10-01','382425');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(33994,01,'1997-07-25','382427');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(49158,01,'2000-05-13','382423');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(22513,01,'2003-09-29','382423');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(11053,0,'2002-04-10','382426');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(27989,01,'2003-03-17','382429');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(11046,01,'1995-10-01','382425');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(13043,01,'1997-07-25','382427');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(11238,0,'2000-05-13','382423');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(11002,01,'2003-09-29','382423');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(12402,01,'2002-04-10','382426');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(13023,01,'2003-03-17','382429');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(11045,01,'1995-10-01','382425');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(14255,01,'1997-07-25','382427');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(14245,0,'2000-05-13','382423');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(22192,01,'2003-09-29','382423');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(12356,0,'2002-04-10','382426');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(11305,01,'2003-03-17','382429');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(12005,01,'1995-10-01','382425');
INSERT INTO "soldiers_status" (sold_id,alive,wardate,pincode) VALUES(12498,01,'2002-04-10','382426');

Posting
SET SEARCH_PATH TO armydb;
insert into posting values (12045,382425,'2012-01-07');
insert into posting values (21040,382425,'2014-04-15');
insert into posting values (22045,382425,'2011-12-26');
insert into posting values (19338,382425,'2012-10-01');
insert into posting values (33728,382425,'2010-03-15');
insert into posting values (12051,382422,'2012-01-22');
insert into posting values (11088,382422,'1995-02-11');
insert into posting values (12498,382422,'2009-01-27');
insert into posting values (22513,382422,'2010-04-19');
insert into posting values (11145,382423,'2014-12-05');
insert into posting values (29603,382423,'2005-10-14');
insert into posting values (11046,382423,'2012-03-16');
INSERT INTO posting VALUES(12300,'382429','2006-07-12');
INSERT INTO posting VALUES(14256,'382429','2010-09-10');
INSERT INTO posting VALUES(13423,'382429','2011-05-10');
INSERT INTO posting VALUES(14345,'382429','2004-07-12');
INSERT INTO posting VALUES(21045,'382429','2001-01-15');
INSERT INTO posting VALUES(21040,'382429','2013-07-12');
INSERT INTO posting VALUES(13045,'382430','2011-01-15');
INSERT INTO posting VALUES(29603,'382430','2015-01-12');
INSERT INTO posting VALUES(12245,'382430','2004-02-10');
INSERT INTO posting VALUES(48563,'382430','2002-05-10');
INSERT INTO posting VALUES(10923,'382430','2011-12-12');
INSERT INTO posting VALUES(12051,'382430','2010-07-11');

Location
SET SEARCH_PATH to armydb;
INSERT INTO location VALUES(382421,'Gandhinagar','Gujarat','India');
INSERT INTO location VALUES(382422,'Allahabad','Uttar Pradesh','India');
INSERT INTO location VALUES(382423,'Bakora Steel City', 'Jharkhand', 'India');
INSERT INTO location VALUES(382424,'patna','Bihar','India');
INSERT INTO location VALUES(382425,'jabalpur','Madhya Pradesh','India');
INSERT INTO location VALUES(382426,'Imphal','Manipur','India');
INSERT INTO location VALUES(382427,'Pune','Mumbai','India');
INSERT INTO location VALUES(382428,'Delhi','Delhi','India');
INSERT INTO location VALUES(382429,'Kargil','J&K','India');
INSERT INTO location VALUES(382430,'Danapur','Bihar','India');
INSERT INTO location VALUES(382431,'Gangtok','Sikkim','India');
INSERT INTO location VALUES(382432,'Ganganagar','Rajasthan','India');
INSERT INTO location VALUES(382433,'Kohima','Nagaland','India');
INSERT INTO location VALUES(382434,'Roorkee','Uttarakhand','India');
INSERT INTO location VALUES(382436,'Durgapur','Westbangal','India');
INSERT INTO location VALUES(382437,'Chiniot','Panjab','India');

Inventory
SET SEARCH_PATH TO armydb;
INSERT INTO "inventory" (weapon_id, sold_id) VALUES ('1053', '19339');
INSERT INTO "inventory" (weapon_id, sold_id) VALUES ('1054', '36099');
INSERT INTO "inventory" (weapon_id, sold_id) VALUES ('1055', '12345');
INSERT INTO "inventory" (weapon_id, sold_id) VALUES ('1056', '28613');
INSERT INTO "inventory" (weapon_id, sold_id) VALUES ('1057', '14256');
INSERT INTO "inventory" (weapon_id, sold_id) VALUES ('1058', '48563');
INSERT INTO "inventory" (weapon_id, sold_id) VALUES ('1059', '33728');
INSERT INTO "inventory" (weapon_id, sold_id) VALUES ('1060', '23432');
INSERT INTO "inventory" (weapon_id, sold_id) VALUES ('1061', '33998');
INSERT INTO "inventory" (weapon_id, sold_id) VALUES ('1062', '40386');
INSERT INTO "inventory" (weapon_id, sold_id) VALUES ('1063', '31931');
INSERT INTO "inventory" (weapon_id, sold_id) VALUES ('1064', '49159');
INSERT INTO "inventory" (weapon_id, sold_id) VALUES ('1065', '19338');
INSERT INTO "inventory" (weapon_id, sold_id) VALUES ('1066', '21474');
INSERT INTO "inventory" (weapon_id, sold_id) VALUES ('1067', '12498');
INSERT INTO "inventory" (weapon_id, sold_id) VALUES ('1068', '14298');
INSERT INTO "inventory" (weapon_id, sold_id) VALUES ('1069', '33994');
INSERT INTO "inventory" (weapon_id, sold_id) VALUES ('1070', '12398');
INSERT INTO "inventory" (weapon_id, sold_id) VALUES ('1071', '13424');
INSERT INTO "inventory" (weapon_id, sold_id) VALUES ('1072', '49158');
INSERT INTO "inventory" (weapon_id, sold_id) VALUES ('1073', '29603');
INSERT INTO "inventory" (weapon_id, sold_id) VALUES ('1074', '22513');
INSERT INTO "inventory" (weapon_id, sold_id) VALUES ('1075', '27989');
INSERT INTO "inventory" (weapon_id, sold_id) VALUES ('1076', '12245');
INSERT INTO "inventory" (weapon_id, sold_id) VALUES ('1077', '10305');
INSERT INTO "inventory" (weapon_id, sold_id) VALUES ('1078', '12051');
INSERT INTO "inventory" (weapon_id, sold_id) VALUES ('1079', '12300');
INSERT INTO "inventory" (weapon_id, sold_id) VALUES ('1080', '10923');
INSERT INTO "inventory" (weapon_id, sold_id) VALUES ('1081', '11053');
INSERT INTO "inventory" (weapon_id, sold_id) VALUES ('1082', '13423');
INSERT INTO "inventory" (weapon_id, sold_id) VALUES ('1083', '12105');
INSERT INTO "inventory" (weapon_id, sold_id) VALUES ('1084', '14345');
INSERT INTO "inventory" (weapon_id, sold_id) VALUES ('1065', '11145');
INSERT INTO "inventory" (weapon_id, sold_id) VALUES ('1066', '12115');
INSERT INTO "inventory" (weapon_id, sold_id) VALUES ('1067', '12045');
INSERT INTO "inventory" (weapon_id, sold_id) VALUES ('1068', '10345');
INSERT INTO "inventory" (weapon_id, sold_id) VALUES ('1069', '10045');
INSERT INTO "inventory" (weapon_id, sold_id) VALUES ('1062', '12005');
INSERT INTO "inventory" (weapon_id, sold_id) VALUES ('1065', '11305');
INSERT INTO "inventory" (weapon_id, sold_id) VALUES ('1064', '11045');
INSERT INTO "inventory" (weapon_id, sold_id) VALUES ('1069', '21045');

Visited
SET SEARCH_PATH TO armydb;
INSERT INTO visited VALUES(19339,'382422','2011-01-10','For a confidential meeting');
INSERT INTO visited VALUES (33998, '382426','2015-10-05','For meeting with a Chinese officer');
INSERT INTO visited VALUES (13423, '382425','2013-05-26','For meeting on movement of pakistan');
INSERT INTO visited VALUES (49159, '382429','2006-12-28','For a meeting of visit of Dalai Lama');
INSERT INTO visited VALUES (29603, '382436','2008-07-12','For reviewing a deal of weapons with Russia');
INSERT INTO visited VALUES (10923, '382429','2005-03-21','For awarding a medal');
INSERT INTO visited VALUES (12300, '382427','2003-11-04','For discussing border-security issues in Capital');
INSERT INTO visited VALUES (11305, '382430','2010-01-05','For a techincal meeting on radar technology with Taiwan');
INSERT INTO visited VALUES (10045, '382431','2013-01-19','For a surgical strike on Pakistan.');
INSERT INTO visited VALUES (12005, '382425','2016-09-30','For a meeting with the naval-chief');
INSERT INTO visited VALUES (11046, '382436','2017-01-31','For a meeting at Indo-Pak Border');
INSERT INTO visited VALUES (13045, '382437','2011-01-17','For a meeting with Air-chief');
INSERT INTO visited VALUES (21045, '382428','2001-10-12','For a confidential meeting');
INSERT INTO visited VALUES (14345, '382422','2016-12-12','For reviewing a deal of weapons with America');
INSERT INTO visited VALUES (12300, '382421','2009-05-19','For a meeting in New-Delhi');
INSERT INTO visited VALUES (14345, '382427','2008-08-05','For a meeting with Chinese officials');
INSERT INTO visited VALUES (12245, '382433','2001-11-24','For a meeting on purchasing new weapons');

Assign
SET SEARCH_PATH TO armydb;
INSERT INTO "assign" (sold_id, type) VALUES ('19339', 'Soldier');
INSERT INTO "assign" (sold_id, type) VALUES ('33998', 'Soldier');
INSERT INTO "assign" (sold_id, type) VALUES ('49159', 'Major General');
INSERT INTO "assign" (sold_id, type) VALUES ('21474', 'Field Marshal');
INSERT INTO "assign" (sold_id, type) VALUES ('12498', 'Soldier');
INSERT INTO "assign" (sold_id, type) VALUES ('14298', 'Lieutenant General');
INSERT INTO "assign" (sold_id, type) VALUES ('12398', 'Soldier');
INSERT INTO "assign" (sold_id, type) VALUES ('13424', 'Soldier');
INSERT INTO "assign" (sold_id, type) VALUES ('28613', 'Soldier');
INSERT INTO "assign" (sold_id, type) VALUES ('13011', 'Captain');
INSERT INTO "assign" (sold_id, type) VALUES ('12300', 'Soldier');
INSERT INTO "assign" (sold_id, type) VALUES ('14256', 'Captain');
INSERT INTO "assign" (sold_id, type) VALUES ('11088', 'Soldier');
INSERT INTO "assign" (sold_id, type) VALUES ('13423', 'Soldier');
INSERT INTO "assign" (sold_id, type) VALUES ('14345', 'Soldier');
INSERT INTO "assign" (sold_id, type) VALUES ('21045', 'Soldier');
INSERT INTO "assign" (sold_id, type) VALUES ('21040', 'Soldier');
INSERT INTO "assign" (sold_id, type) VALUES ('22045', 'Major');
INSERT INTO "assign" (sold_id, type) VALUES ('13045', 'Havildar');
INSERT INTO "assign" (sold_id, type) VALUES ('29603', 'Soldier');
INSERT INTO "assign" (sold_id, type) VALUES ('12245', 'Soldier');
INSERT INTO "assign" (sold_id, type) VALUES ('10305', 'Captain');
INSERT INTO "assign" (sold_id, type) VALUES ('48563', 'Colonel');
INSERT INTO "assign" (sold_id, type) VALUES ('10923', 'Major General');
INSERT INTO "assign" (sold_id, type) VALUES ('12051', 'Soldier');
INSERT INTO "assign" (sold_id, type) VALUES ('12105', 'Major');
INSERT INTO "assign" (sold_id, type) VALUES ('11145', 'Brigadier');
INSERT INTO "assign" (sold_id, type) VALUES ('12115', 'Soldier');
INSERT INTO "assign" (sold_id, type) VALUES ('12045', 'Soldier');
INSERT INTO "assign" (sold_id, type) VALUES ('10345', 'Lieutenant');
INSERT INTO "assign" (sold_id, type) VALUES ('10045', 'Soldier');
INSERT INTO "assign" (sold_id, type) VALUES ('36099', 'Havildar');
INSERT INTO "assign" (sold_id, type) VALUES ('12345', 'Lieutenant');
INSERT INTO "assign" (sold_id, type) VALUES ('33728', 'Brigadier');
INSERT INTO "assign" (sold_id, type) VALUES ('23432', 'Soldier');
INSERT INTO "assign" (sold_id, type) VALUES ('40386', 'Soldier');
INSERT INTO "assign" (sold_id, type) VALUES ('31931', 'Soldier');
INSERT INTO "assign" (sold_id, type) VALUES ('19338', 'Soldier');
INSERT INTO "assign" (sold_id, type) VALUES ('33994', 'Soldier');
INSERT INTO "assign" (sold_id, type) VALUES ('49158', 'Captain');
INSERT INTO "assign" (sold_id, type) VALUES ('22513', 'Soldier');
INSERT INTO "assign" (sold_id, type) VALUES ('11053', 'Soldier');
INSERT INTO "assign" (sold_id, type) VALUES ('27989', 'Captain');
INSERT INTO "assign" (sold_id, type) VALUES ('11046', 'Captain');
INSERT INTO "assign" (sold_id, type) VALUES ('13043', 'Soldier');
INSERT INTO "assign" (sold_id, type) VALUES ('11238', 'Captain');
INSERT INTO "assign" (sold_id, type) VALUES ('11002', 'Soldier');
INSERT INTO "assign" (sold_id, type) VALUES ('12402', 'Captain');
INSERT INTO "assign" (sold_id, type) VALUES ('13023', 'Soldier');
INSERT INTO "assign" (sold_id, type) VALUES ('11045', 'Soldier');
INSERT INTO "assign" (sold_id, type) VALUES ('14255', 'Captain');
INSERT INTO "assign" (sold_id, type) VALUES ('14245', 'Soldier');
INSERT INTO "assign" (sold_id, type) VALUES ('22192', 'Soldier');
INSERT INTO "assign" (sold_id, type) VALUES ('12356', 'Captain');
INSERT INTO "assign" (sold_id, type) VALUES ('11305', 'Havildar');
INSERT INTO "assign" (sold_id, type) VALUES ('12005', 'Colonel');
INSERT INTO "assign" (sold_id, type) VALUES ('12498', 'Soldier');






 
RESULT
 
ADD NEW: 
If we want to add any soldier information, then first we need to fill out all the fields on the left hand side and then press ‘ADD NEW’; this will add the new soldier information in the database and will be displayed on the scroll bar on the right hand side.
DISPLAY: 
If we want o display and soldier information then we simply need to click on display and the scroll bar menu will appear automatically on the Right Hand Side, we can scroll and click on any soldier name, that particular soldier’s information will appear on the Left Hand Side of the screen.
CLEAR: 
If we want to rid the screen of any information that is not needed at the instance we just need to click on ‘CLEAR’ and the left hand side of the screen will be cleared of all information. 
SEARCH:
 If we want to search any information about a particular soldier then put the Soldier Id of that soldier in the corresponding field and press ‘SEARCH’, this will give the entire soldier information available and display on the Left Hand Side.
DELETE: 
If we want to delete any solider information no matter for what so ever reason it can be, Dis-honourable discharge from duty, retirement, KIA (Killed in Action), MIA (Missing in Action), etc. All we need to do is select that particular soldier’s information from the scroll menu and press ‘DELETE’, the information will be deleted from the database itself.
UPDATE:
If we want to update any soldier’s information due to any reason like promotion, change in battalion, all we need to do is select that soldiers information from the scroll menu on the Right Hand Side , make the necessary changes in his or her information on the Left Hand Side and press ‘UPDATE’.
EXIT:
If we need to Exit the Database then simply press on ‘EXIT’ and the database will give a message box saying, “Do you want to EXIT the ARMED FORCES DBMS”, Are you Sure??? Yes OR No”, Press on ‘YES’ if you really want to exit the database or either press ‘NO’ and continue using the ‘ARMED FORCES DATABASE’. 

