DROP DATABASE aimslogin;

CREATE DATABASE IF NOT EXISTS `aimslogin` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `aimslogin`;

CREATE TABLE IF NOT EXISTS `accounts` 
(
	`id` int(11) NOT NULL AUTO_INCREMENT,
    `first_name` VARCHAR(50) NOT NULL,
    `last_name` VARCHAR(50) NOT NULL,
    `phone` BIGINT NOT NULL,
    `email` VARCHAR(100) NOT NULL,
    `address` VARCHAR(300),
    `password` VARCHAR(255) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB AUTO_INCREMENT = 2 DEFAULT CHARSET = utf8;

INSERT INTO accounts(first_name,last_name,phone,email,address,password) VALUES
('Mahesh','Amdekar', 9987364883,'ma@gmail.com',NULL, 0101),
('Manasi','Amdekar', 9987294883,'mva@gmail.com','xyz',2222),
('Aabha','Padave', 9982316453,'ap@gmail.com','abc',3333),
('Rakesh','Chaudhary', 5568743583,'rc@gmail.com','def',4444),
('Manisha','Khande', 1290364883,'mk@gmail.com','ghi',5555),
('Sanika','Patankar', 7493874883,'sp@gmail.com','jkl',6666),
('Aditya','Patankar', 6354271829,'ap@gmail.com','mno',7777),
('Vishwanath','Karandikar', 8837459283,'vk@gmail.com','pqr',8888),
('Kritika','Kundra', 8374927391,'kk@gmail.com','stw',9999),
('Carol','Sylas', 7382937483,'cs@gmail.com','xjgshcv',1010),
('Kenneth','Sebastian', 5463377289,'ks@gmail.com',NULL,1111),
('Sai','Patwardhan', 9040372839,'spp@gmail.com','khsbdouhj',1212),
('Sakshi','Motwani', 6758497289,'sm@gmail.com','klwjbouchb',1313),
('Sahil','Yadav', 9904738625,'sy@gmail.com',NULL,1414),
('Trupti','Verma', 4035467897,'tv@gmail.com','jkwueyuiqhnlk',1515),
('Tripura','Paralikar', 7362537283,'tp@gmail.com','joshbc hjqdbxkh',1616),
('Anuj','Todkar', 647583940,'at@gmail.com','wjkbhdckw',1717),
('Chinmay','Kasture', 2637837465,'ck@gmail.com',NULL,1818),
('Vallari','Dhapre', 8847336293,'vd@gmail.com',NULL,1919),
('Sarthak','Chatterjee', 7384635234,'sc@gmail.com','lbwudc qiwubx lquisxhnwjhd',2020);
 
 DROP TABLE accounts;
 select * from accounts;
