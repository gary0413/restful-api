use `test`;

CREATE TABLE IF NOT EXISTS `tracking_details` (
  `id` int NOT NULL AUTO_INCREMENT,
  `sno` int DEFAULT NULL,
  `date` varchar(512) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `time` varchar(512) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `status` varchar(512) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `location_id` int DEFAULT NULL,
  `location_title` varchar(512) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1249 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `tracking_details` (`id`, `sno`, `date`, `time`, `status`, `location_id`, `location_title`) VALUES
	(1234, 123456789, '2023-03-30', '14:00', 'Package Received', 1, '花蓮物流中心'),
	(1235, 123456789, '2023-03-31', '10:30', 'In Transit', 7, '台北物流中心'),
	(1236, 123456789, '2023-04-01', '16:45', 'Out for Delivery', 18, '高雄物流中心'),
	(1237, 123456789, '2023-04-02', '09:15', 'Delivered', 4, '台南物流中心'),
	(1238, 179765, '2023-12-03', '12:00', 'Exception', 9, NULL),
	(1243, 630025, '2023-12-03', '12:00', 'Delivery Attempted', 24, NULL),
	(1244, 289167, '2023-12-03', '12:00', 'Delivery Attempted', 23, NULL),
	(1245, 991040, '2023-12-03', '12:00', 'Created', 24, NULL),
	(1246, 527300, '2023-12-03', '12:00', 'Delivery Attempted', 11, NULL),
	(1247, 480738, '2023-12-03', '12:00', 'Delivery Attempted', 9, NULL),
	(1248, 143008, '2023-12-03', '12:00', 'In Transit', 4, NULL);

