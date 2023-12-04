use `test`;

DROP TABLE IF EXISTS `admins`;

CREATE TABLE IF NOT EXISTS `locations` (
  `location_id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(512) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `city` varchar(512) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `address` varchar(512) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`location_id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


INSERT INTO `locations` (`location_id`, `title`, `city`, `address`) VALUES
	(1, '花蓮物流中心', '花蓮市', '花蓮市國聯一路100號'),
	(3, '桃園物流中心', '桃園市', '桃園市中壢區中央西路三段150號'),
	(4, '台南物流中心', '台南市', '台南市安平區建平路18號'),
	(6, '宜蘭物流中心', '宜蘭市', '宜蘭市中山路二段58號'),
	(7, '台北物流中心', '台北市', '台北市中正區忠孝東路100號'),
	(8, '澎湖物流中心', '澎湖縣', '澎湖縣馬公市中正路200號'),
	(9, '彰化物流中心', '彰化市', '彰化市中山路二段250號'),
	(11, '南投物流中心', '南投市', '南投市自由路67號'),
	(13, '新竹物流中心', '新竹市', '新竹市東區光復路一段101號'),
	(14, '基隆物流中心', '基隆市', '基隆市信一路50號'),
	(15, '嘉義物流中心', '嘉義市', '嘉義市東區民族路380號'),
	(18, '高雄物流中心', '高雄市', '高雄市前金區成功一路82號'),
	(19, '金門物流中心', '金門縣', '金門縣金城鎮民生路90號'),
	(21, '屏東物流中心', '屏東市', '屏東市民生路300號'),
	(23, '雲林物流中心', '雲林市', '雲林市中正路五段120號'),
	(24, '台中物流中心', '台中市', '台中市西區民生路200號');
