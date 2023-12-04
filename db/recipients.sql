use `test`;

CREATE TABLE IF NOT EXISTS `recipients` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(512) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `address` varchar(512) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `phone` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1252 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `recipients` (`id`, `name`, `address`, `phone`) VALUES
	(1234, '賴小賴', '台北市中正區仁愛路二段99號', 91234567),
	(1235, '陳大明', '新北市板橋區文化路一段100號', 92345678),
	(1236, '林小芳', '台中市西區民生路200號', 93456789),
	(1237, '張美玲', '高雄市前金區成功一路82號', 94567890),
	(1238, '王小明', '台南市安平區建平路18號', 95678901),
	(1239, '劉大華', '新竹市東區光復路一段101號', 96789012),
	(1240, '黃小琳', '彰化市中山路二段250號', 97890123),
	(1241, '吳美美', '花蓮市國聯一路100號', 98901234),
	(1242, '蔡小虎', '屏東市民生路300號', 99012345),
	(1243, '鄭大勇', '基隆市信一路50號', 91123456),
	(1244, '謝小珍', '嘉義市東區民族路380號', 92234567),
	(1245, '潘大為', '宜蘭市中山路二段58號', 93345678),
	(1246, '趙小梅', '南投市自由路67號', 94456789),
	(1247, '周小龍', '雲林市中正路五段120號', 95567890),
	(1248, '李大同', '澎湖縣馬公市中正路200號', 96678901),
	(1249, '陳小凡', '金門縣金城鎮民生路90號', 97789012),
	(1250, '楊大明', '台北市信義區松仁路50號', 98890123),
	(1251, '吳小雯', '新北市中和區景平路100號', 99901234);
