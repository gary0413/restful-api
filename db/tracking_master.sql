use `test`;

CREATE TABLE IF NOT EXISTS `tracking_master` (
  `sno` int NOT NULL,
  `tracking_status` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `estimated_delivery` date NOT NULL,
  `recipient_id` int NOT NULL,
  `current_location_id` int NOT NULL,
  PRIMARY KEY (`sno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `tracking_master` (`sno`, `tracking_status`, `estimated_delivery`, `recipient_id`, `current_location_id`) VALUES
	(143008, 'In Transit', '2023-12-03', 1244, 4),
	(179765, 'Exception', '2023-12-03', 1243, 9),
	(289167, 'Delivery Attempted', '2023-12-03', 1246, 23),
	(480738, 'Delivery Attempted', '2023-12-03', 1235, 9),
	(527300, 'Delivery Attempted', '2023-12-03', 1242, 11),
	(630025, 'Delivery Attempted', '2023-12-03', 1239, 24),
	(991040, 'Created', '2023-12-03', 1251, 24),
	(123456789, 'In Transit', '2023-04-05', 1234, 13);
