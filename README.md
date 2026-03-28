# EM-GUI
PyQT GUI for the Electricity Meter

## Configuration
The DB Configuration is stored in a local config file "config.ini", which has to
be created before starting the program the first time. As an example "config.ini.example"
is delivered.


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
