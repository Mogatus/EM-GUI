# EM-GUI
PyQT GUI for the Electricity Meter

## SQL-Statement for MySQL
CREATE TABLE `meter_data` (
	`id` INT(11) NOT NULL AUTO_INCREMENT,
	`loadVal` INT(11) NULL DEFAULT NULL,
	`pv` INT(11) NULL DEFAULT NULL,
	`grid_feed_in` INT(11) NULL DEFAULT NULL,
	`grid_purchase` INT(11) NULL DEFAULT NULL,
	`saveTimestamp` VARCHAR(32) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
	PRIMARY KEY (`id`) USING BTREE
)
COLLATE='utf8mb4_general_ci'
ENGINE=InnoDB
AUTO_INCREMENT=189
;
