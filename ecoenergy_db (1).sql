-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 09-10-2025 a las 14:48:38
-- Versión del servidor: 9.1.0
-- Versión de PHP: 8.3.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `ecoenergy_db`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `auth_group`
--

INSERT INTO `auth_group` (`id`, `name`) VALUES
(1, 'LimitedUser');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `auth_group_permissions`
--

INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES
(1, 1, 44),
(2, 1, 36);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add category', 7, 'add_category'),
(26, 'Can change category', 7, 'change_category'),
(27, 'Can delete category', 7, 'delete_category'),
(28, 'Can view category', 7, 'view_category'),
(29, 'Can add organization', 8, 'add_organization'),
(30, 'Can change organization', 8, 'change_organization'),
(31, 'Can delete organization', 8, 'delete_organization'),
(32, 'Can view organization', 8, 'view_organization'),
(33, 'Can add device', 9, 'add_device'),
(34, 'Can change device', 9, 'change_device'),
(35, 'Can delete device', 9, 'delete_device'),
(36, 'Can view device', 9, 'view_device'),
(37, 'Can add measurement', 10, 'add_measurement'),
(38, 'Can change measurement', 10, 'change_measurement'),
(39, 'Can delete measurement', 10, 'delete_measurement'),
(40, 'Can view measurement', 10, 'view_measurement'),
(41, 'Can add alert', 11, 'add_alert'),
(42, 'Can change alert', 11, 'change_alert'),
(43, 'Can delete alert', 11, 'delete_alert'),
(44, 'Can view alert', 11, 'view_alert'),
(45, 'Can add zone', 12, 'add_zone'),
(46, 'Can change zone', 12, 'change_zone'),
(47, 'Can delete zone', 12, 'delete_zone'),
(48, 'Can view zone', 12, 'view_zone');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(2, 'pbkdf2_sha256$1000000$7AWqGlY5bJUEehxt3ZAKzn$YjMc7iNGYnMw0tUJ4Ilmk5ey4HxV3KvIzICJW2N755Y=', '2025-10-09 14:34:47.839462', 1, 'gsk', '', '', 'gsk@ecoenergy.cl', 1, 1, '2025-10-09 02:49:48.100783'),
(3, 'pbkdf2_sha256$1000000$E2XVcLXrdKyTUv8cqsNY3K$muxGBwmU/9vGQf6lFII4hpxQllWcwswwCQdcgcXFAV0=', '2025-10-09 14:30:51.968785', 0, 'pnk', 'Juan', 'Perez', 'pnk@ecoenergy.cl', 1, 1, '2025-10-09 02:50:38.000000'),
(4, 'pbkdf2_sha256$1000000$ep12a1BQ9epiT80kyyXdUy$14E96wvz5TTaZPZKp8P6Ib3oRZly6w2avJY2dF4f2JM=', NULL, 1, 'jahumada', '', '', 'jahumada@ecoenergy.cl', 1, 1, '2025-10-09 02:52:12.530727');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `auth_user_groups`
--

INSERT INTO `auth_user_groups` (`id`, `user_id`, `group_id`) VALUES
(1, 3, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dispositivos_alert`
--

DROP TABLE IF EXISTS `dispositivos_alert`;
CREATE TABLE IF NOT EXISTS `dispositivos_alert` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `device_id` bigint NOT NULL,
  `organization_id` bigint NOT NULL,
  `alert_level` varchar(10) NOT NULL,
  `message` varchar(255) NOT NULL,
  `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_alert_device` (`device_id`),
  KEY `fk_alert_organization` (`organization_id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `dispositivos_alert`
--

INSERT INTO `dispositivos_alert` (`id`, `device_id`, `organization_id`, `alert_level`, `message`, `date`, `created_at`, `updated_at`, `deleted_at`) VALUES
(38, 3, 2, 'Low', 'Sensor requiere mantenimiento', '2025-10-07 01:01:32', '2025-10-07 01:01:32', '2025-10-07 01:01:32', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dispositivos_category`
--

DROP TABLE IF EXISTS `dispositivos_category`;
CREATE TABLE IF NOT EXISTS `dispositivos_category` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `organization_id` bigint NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_category_org` (`organization_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `dispositivos_category`
--

INSERT INTO `dispositivos_category` (`id`, `name`, `organization_id`, `created_at`, `updated_at`, `deleted_at`) VALUES
(1, 'Solar', 1, '2025-10-09 14:04:30', '2025-10-09 14:04:30', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dispositivos_device`
--

DROP TABLE IF EXISTS `dispositivos_device`;
CREATE TABLE IF NOT EXISTS `dispositivos_device` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `category_id` bigint DEFAULT NULL,
  `zone_id` bigint DEFAULT NULL,
  `organization_id` bigint NOT NULL,
  `created_at` datetime(6) DEFAULT CURRENT_TIMESTAMP(6),
  `updated_at` datetime(6) DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  `deleted_at` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `dispositivos_device_organization_id_idx` (`organization_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `dispositivos_device`
--

INSERT INTO `dispositivos_device` (`id`, `name`, `category_id`, `zone_id`, `organization_id`, `created_at`, `updated_at`, `deleted_at`) VALUES
(3, 'Sensor A1', 1, 1, 1, '2025-10-09 01:01:23.000000', '2025-10-09 14:43:00.739694', '2025-10-09 14:42:59.000000'),
(5, 'Sensor A2', 1, 2, 2, '2025-10-09 14:42:29.355142', '2025-10-09 14:42:55.194380', '2025-10-09 14:42:53.000000');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dispositivos_measurement`
--

DROP TABLE IF EXISTS `dispositivos_measurement`;
CREATE TABLE IF NOT EXISTS `dispositivos_measurement` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `device_id` bigint NOT NULL,
  `value` decimal(10,2) NOT NULL,
  `measured_at` datetime NOT NULL,
  `organization_id` bigint NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_measurement_device` (`device_id`),
  KEY `fk_measurement_org` (`organization_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `dispositivos_measurement`
--

INSERT INTO `dispositivos_measurement` (`id`, `device_id`, `value`, `measured_at`, `organization_id`, `created_at`, `updated_at`, `deleted_at`) VALUES
(1, 3, 1.93, '2025-10-09 14:08:07', 1, '2025-10-09 14:08:44', '2025-10-09 14:08:44', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dispositivos_organization`
--

DROP TABLE IF EXISTS `dispositivos_organization`;
CREATE TABLE IF NOT EXISTS `dispositivos_organization` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `password` varchar(128) COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `address` varchar(200) COLLATE utf8mb4_general_ci NOT NULL,
  `created_at` datetime(6) DEFAULT CURRENT_TIMESTAMP(6),
  `updated_at` datetime(6) DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  `deleted_at` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `dispositivos_organization`
--

INSERT INTO `dispositivos_organization` (`id`, `name`, `password`, `email`, `address`, `created_at`, `updated_at`, `deleted_at`) VALUES
(1, 'EcoEnergy', 'mañeñoñaño', 'gsk@ecoenergy.cl', 'Calle Zoidberg 771', '2025-10-08 23:05:47.476903', '2025-10-09 14:46:46.336104', '2025-10-09 14:46:45.000000'),
(2, 'SolarX', 'mañeño', 'selfdestructor@gmail.com', 'Av. Las Mandarinas 9851', '2025-10-09 01:01:23.000000', '2025-10-09 14:46:40.946464', '2025-10-09 14:46:39.000000');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dispositivos_zone`
--

DROP TABLE IF EXISTS `dispositivos_zone`;
CREATE TABLE IF NOT EXISTS `dispositivos_zone` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `organization_id` bigint NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_zone_org` (`organization_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `dispositivos_zone`
--

INSERT INTO `dispositivos_zone` (`id`, `name`, `organization_id`, `created_at`, `updated_at`, `deleted_at`) VALUES
(1, 'Norte', 1, '2025-10-09 14:06:49', '2025-10-09 14:06:49', NULL),
(2, 'Sur', 2, '2025-10-09 14:42:25', '2025-10-09 14:42:25', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ;

--
-- Volcado de datos para la tabla `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2025-10-09 13:28:47.269684', '1', 'LimitedUser', 1, '[{\"added\": {}}]', 3, 2),
(2, '2025-10-09 13:29:06.431781', '1', 'LimitedUser', 2, '[]', 3, 2),
(3, '2025-10-09 13:31:01.611003', '3', 'pnk', 2, '[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Superuser status\", \"Groups\"]}}]', 4, 2),
(4, '2025-10-09 13:32:43.677274', '3', 'pnk', 2, '[{\"changed\": {\"fields\": [\"password\"]}}]', 4, 2),
(5, '2025-10-09 13:32:58.409650', '3', 'pnk', 2, '[]', 4, 2),
(6, '2025-10-09 14:04:29.538177', '1', 'Category object (1)', 1, '[{\"added\": {}}]', 7, 2),
(7, '2025-10-09 14:06:49.175062', '1', 'Zone object (1)', 1, '[{\"added\": {}}]', 12, 2),
(8, '2025-10-09 14:07:17.554491', '1', 'Organization object (1)', 2, '[{\"changed\": {\"fields\": [\"Email\", \"Password\"]}}]', 8, 2),
(9, '2025-10-09 14:07:34.850425', '3', 'Device object (3)', 2, '[]', 9, 2),
(10, '2025-10-09 14:08:44.046595', '1', 'Measurement object (1)', 1, '[{\"added\": {}}]', 10, 2),
(11, '2025-10-09 14:10:01.460990', '3', 'Device object (3)', 2, '[]', 9, 2),
(12, '2025-10-09 14:36:55.917162', '2', 'Organization object (2)', 2, '[{\"changed\": {\"fields\": [\"Email\", \"Password\"]}}]', 8, 2),
(13, '2025-10-09 14:37:12.392422', '1', 'Organization object (1)', 2, '[{\"changed\": {\"fields\": [\"Password\"]}}]', 8, 2),
(14, '2025-10-09 14:42:24.902363', '2', 'Zone object (2)', 1, '[{\"added\": {}}]', 12, 2),
(15, '2025-10-09 14:42:29.355418', '5', 'Device object (5)', 1, '[{\"added\": {}}]', 9, 2),
(16, '2025-10-09 14:42:55.194771', '5', 'Device object (5)', 2, '[{\"changed\": {\"fields\": [\"Deleted at\"]}}]', 9, 2),
(17, '2025-10-09 14:43:00.740073', '3', 'Device object (3)', 2, '[{\"changed\": {\"fields\": [\"Deleted at\"]}}]', 9, 2),
(18, '2025-10-09 14:46:40.947004', '2', 'Organization object (2)', 2, '[{\"changed\": {\"fields\": [\"Deleted at\"]}}]', 8, 2),
(19, '2025-10-09 14:46:46.336481', '1', 'Organization object (1)', 2, '[{\"changed\": {\"fields\": [\"Deleted at\"]}}]', 8, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'dispositivos', 'category'),
(8, 'dispositivos', 'organization'),
(9, 'dispositivos', 'device'),
(10, 'dispositivos', 'measurement'),
(11, 'dispositivos', 'alert'),
(12, 'dispositivos', 'zone');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2025-10-09 00:14:32.076664'),
(2, 'auth', '0001_initial', '2025-10-09 00:14:32.266114'),
(3, 'admin', '0001_initial', '2025-10-09 00:14:32.320851'),
(4, 'admin', '0002_logentry_remove_auto_add', '2025-10-09 00:14:32.323847'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2025-10-09 00:14:32.326349'),
(6, 'contenttypes', '0002_remove_content_type_name', '2025-10-09 00:14:32.362366'),
(7, 'auth', '0002_alter_permission_name_max_length', '2025-10-09 00:14:32.373707'),
(8, 'auth', '0003_alter_user_email_max_length', '2025-10-09 00:14:32.385749'),
(9, 'auth', '0004_alter_user_username_opts', '2025-10-09 00:14:32.388432'),
(10, 'auth', '0005_alter_user_last_login_null', '2025-10-09 00:14:32.400563'),
(11, 'auth', '0006_require_contenttypes_0002', '2025-10-09 00:14:32.400945'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2025-10-09 00:14:32.403468'),
(13, 'auth', '0008_alter_user_username_max_length', '2025-10-09 00:14:32.417467'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2025-10-09 00:14:32.433400'),
(15, 'auth', '0010_alter_group_name_max_length', '2025-10-09 00:14:32.445646'),
(16, 'auth', '0011_update_proxy_permissions', '2025-10-09 00:14:32.448196'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2025-10-09 00:14:32.460639'),
(18, 'sessions', '0001_initial', '2025-10-09 00:21:39.054306'),
(19, 'dispositivos', '0001_initial', '2025-10-09 02:02:34.967433');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('gx9z671fu5rklzput1bfu6yhtugtvgx3', '.eJxVjEEOwiAQRe_C2hCGMiAu3XsGwgwgVUOT0q6Md7dNutDtf-_9twhxXWpYe57DmMRFaHH63SjyM7cdpEds90ny1JZ5JLkr8qBd3qaUX9fD_TuosdetVta5YtgVIjCez8zeoALPBhMRgrWGtS4JAAYTEdzmIwwWuXhlPYvPF8_8Nuo:1v6rjD:0re8Vjoa6YSHFNUyGTvYKRxiugH6MNgq4ESSZLnWzbw', '2025-10-23 14:34:47.839981');

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `dispositivos_alert`
--
ALTER TABLE `dispositivos_alert`
  ADD CONSTRAINT `fk_alert_device` FOREIGN KEY (`device_id`) REFERENCES `dispositivos_device` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `fk_alert_organization` FOREIGN KEY (`organization_id`) REFERENCES `dispositivos_organization` (`id`) ON DELETE CASCADE;

--
-- Filtros para la tabla `dispositivos_device`
--
ALTER TABLE `dispositivos_device`
  ADD CONSTRAINT `dispositivos_device_organization_fk` FOREIGN KEY (`organization_id`) REFERENCES `dispositivos_organization` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
