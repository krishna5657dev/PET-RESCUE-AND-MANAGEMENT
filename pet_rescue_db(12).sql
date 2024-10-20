-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 25, 2023 at 10:17 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.0.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pet_rescue_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
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
(25, 'Can add adoption_center_register', 7, 'add_adoption_center_register'),
(26, 'Can change adoption_center_register', 7, 'change_adoption_center_register'),
(27, 'Can delete adoption_center_register', 7, 'delete_adoption_center_register'),
(28, 'Can view adoption_center_register', 7, 'view_adoption_center_register'),
(29, 'Can add adoption_info', 8, 'add_adoption_info'),
(30, 'Can change adoption_info', 8, 'change_adoption_info'),
(31, 'Can delete adoption_info', 8, 'delete_adoption_info'),
(32, 'Can view adoption_info', 8, 'view_adoption_info'),
(33, 'Can add complaint', 9, 'add_complaint'),
(34, 'Can change complaint', 9, 'change_complaint'),
(35, 'Can delete complaint', 9, 'delete_complaint'),
(36, 'Can view complaint', 9, 'view_complaint'),
(37, 'Can add country', 10, 'add_country'),
(38, 'Can change country', 10, 'change_country'),
(39, 'Can delete country', 10, 'delete_country'),
(40, 'Can view country', 10, 'view_country'),
(41, 'Can add district', 11, 'add_district'),
(42, 'Can change district', 11, 'change_district'),
(43, 'Can delete district', 11, 'delete_district'),
(44, 'Can view district', 11, 'view_district'),
(45, 'Can add feedback', 12, 'add_feedback'),
(46, 'Can change feedback', 12, 'change_feedback'),
(47, 'Can delete feedback', 12, 'delete_feedback'),
(48, 'Can view feedback', 12, 'view_feedback'),
(49, 'Can add login', 13, 'add_login'),
(50, 'Can change login', 13, 'change_login'),
(51, 'Can delete login', 13, 'delete_login'),
(52, 'Can view login', 13, 'view_login'),
(53, 'Can add pets', 14, 'add_pets'),
(54, 'Can change pets', 14, 'change_pets'),
(55, 'Can delete pets', 14, 'delete_pets'),
(56, 'Can view pets', 14, 'view_pets'),
(57, 'Can add rescue_info', 15, 'add_rescue_info'),
(58, 'Can change rescue_info', 15, 'change_rescue_info'),
(59, 'Can delete rescue_info', 15, 'delete_rescue_info'),
(60, 'Can view rescue_info', 15, 'view_rescue_info'),
(61, 'Can add user_register', 16, 'add_user_register'),
(62, 'Can change user_register', 16, 'change_user_register'),
(63, 'Can delete user_register', 16, 'delete_user_register'),
(64, 'Can view user_register', 16, 'view_user_register'),
(65, 'Can add state', 17, 'add_state'),
(66, 'Can change state', 17, 'change_state'),
(67, 'Can delete state', 17, 'delete_state'),
(68, 'Can view state', 17, 'view_state'),
(69, 'Can add place', 18, 'add_place'),
(70, 'Can change place', 18, 'change_place'),
(71, 'Can delete place', 18, 'delete_place'),
(72, 'Can view place', 18, 'view_place'),
(73, 'Can add boarding_service', 19, 'add_boarding_service'),
(74, 'Can change boarding_service', 19, 'change_boarding_service'),
(75, 'Can delete boarding_service', 19, 'delete_boarding_service'),
(76, 'Can view boarding_service', 19, 'view_boarding_service'),
(77, 'Can add grooming_service', 20, 'add_grooming_service'),
(78, 'Can change grooming_service', 20, 'change_grooming_service'),
(79, 'Can delete grooming_service', 20, 'delete_grooming_service'),
(80, 'Can view grooming_service', 20, 'view_grooming_service'),
(81, 'Can add booking_boarding', 21, 'add_booking_boarding'),
(82, 'Can change booking_boarding', 21, 'change_booking_boarding'),
(83, 'Can delete booking_boarding', 21, 'delete_booking_boarding'),
(84, 'Can view booking_boarding', 21, 'view_booking_boarding'),
(85, 'Can add booking_grooming', 22, 'add_booking_grooming'),
(86, 'Can change booking_grooming', 22, 'change_booking_grooming'),
(87, 'Can delete booking_grooming', 22, 'delete_booking_grooming'),
(88, 'Can view booking_grooming', 22, 'view_booking_grooming');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$390000$3edGLxxgzkwiF8z1ChIllz$om/tFrEbV9U1KmIELI90B7iihR15iu6tULH7buMuhqA=', NULL, 1, 'admin', '', '', 'admin@gmail.com', 1, 1, '2023-03-04 04:38:44.942533');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(7, 'PetRescueApp', 'adoption_center_register'),
(8, 'PetRescueApp', 'adoption_info'),
(19, 'PetRescueApp', 'boarding_service'),
(21, 'PetRescueApp', 'booking_boarding'),
(22, 'PetRescueApp', 'booking_grooming'),
(9, 'PetRescueApp', 'complaint'),
(10, 'PetRescueApp', 'country'),
(11, 'PetRescueApp', 'district'),
(12, 'PetRescueApp', 'feedback'),
(20, 'PetRescueApp', 'grooming_service'),
(13, 'PetRescueApp', 'login'),
(14, 'PetRescueApp', 'pets'),
(18, 'PetRescueApp', 'place'),
(15, 'PetRescueApp', 'rescue_info'),
(17, 'PetRescueApp', 'state'),
(16, 'PetRescueApp', 'user_register'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'PetRescueApp', '0001_initial', '2023-03-04 04:37:11.929928'),
(2, 'contenttypes', '0001_initial', '2023-03-04 04:37:11.976796'),
(3, 'auth', '0001_initial', '2023-03-04 04:37:12.315296'),
(4, 'admin', '0001_initial', '2023-03-04 04:37:12.431174'),
(5, 'admin', '0002_logentry_remove_auto_add', '2023-03-04 04:37:12.446809'),
(6, 'admin', '0003_logentry_add_action_flag_choices', '2023-03-04 04:37:12.462411'),
(7, 'contenttypes', '0002_remove_content_type_name', '2023-03-04 04:37:12.531409'),
(8, 'auth', '0002_alter_permission_name_max_length', '2023-03-04 04:37:12.578273'),
(9, 'auth', '0003_alter_user_email_max_length', '2023-03-04 04:37:12.593895'),
(10, 'auth', '0004_alter_user_username_opts', '2023-03-04 04:37:12.609518'),
(11, 'auth', '0005_alter_user_last_login_null', '2023-03-04 04:37:12.647299'),
(12, 'auth', '0006_require_contenttypes_0002', '2023-03-04 04:37:12.662921'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2023-03-04 04:37:12.662921'),
(14, 'auth', '0008_alter_user_username_max_length', '2023-03-04 04:37:12.678546'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2023-03-04 04:37:12.709786'),
(16, 'auth', '0010_alter_group_name_max_length', '2023-03-04 04:37:12.716298'),
(17, 'auth', '0011_update_proxy_permissions', '2023-03-04 04:37:12.731943'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2023-03-04 04:37:12.763207'),
(19, 'sessions', '0001_initial', '2023-03-04 04:37:12.778790'),
(20, 'PetRescueApp', '0002_boarding_service', '2023-03-04 09:40:12.717596'),
(21, 'PetRescueApp', '0003_grooming_service', '2023-03-05 15:55:07.519341'),
(22, 'PetRescueApp', '0004_booking_boarding', '2023-03-06 06:48:13.634200'),
(23, 'PetRescueApp', '0005_booking_grooming', '2023-03-06 09:41:21.469744');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('l8c0wczg7g0vykygd997151m7m5a9s1n', 'eyJzdW5hbWUiOiJhbnUxMjMiLCJzbG9naWQiOjF9:1poiye:UB22K1hc7uEgHhzejrPCBWYqh3Pvc403sCYznru9JXA', '2023-05-02 10:54:24.680161'),
('m1vug2b6zhogjws67dx9i10tbbj68wsf', 'eyJzdW5hbWUiOiJhbnUxMjMiLCJzbG9naWQiOjF9:1pZ2MT:JBVPUSPNXjcycUCvNjdHS32uEaO3b7ctJODcWNpksJI', '2023-03-20 04:22:09.971840'),
('s0kx8h69bmmzc83wtvu4b9p2jeg67isc', 'eyJzdW5hbWUiOiJhbnUxMjMiLCJzbG9naWQiOjF9:1prDqA:gqhhSqaPyhOPlVb_-mGxIFmJXKi-iE_Kfn6jqfOfyPM', '2023-05-09 08:15:58.335671'),
('v6wb6pi5mq506ebnh7n4vd4hf9tgfnl5', 'eyJzdW5hbWUiOiJhbnUxMjMiLCJzbG9naWQiOjF9:1poKZe:kBp8CpBPf6kKTvHaWhIpeD3ctjTPOJdVkO4h0lDsk20', '2023-05-01 08:50:58.483864'),
('wbtu7pqxwzqw711w0dm11ne573wk7q2a', 'eyJzdW5hbWUiOiJhbnUxMjMiLCJzbG9naWQiOjF9:1poL1f:kM7vIP3x91uWtMDG_2shHy4YdI0q8G2UFM5yfQQRM7E', '2023-05-01 09:19:55.436298');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_adoption`
--

CREATE TABLE `tbl_adoption` (
  `adoption_id` int(11) NOT NULL,
  `pet_type` varchar(50) NOT NULL,
  `tag_name` varchar(50) NOT NULL,
  `breed` varchar(50) NOT NULL,
  `age` int(11) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `date` date NOT NULL,
  `photo` varchar(50) NOT NULL,
  `Ac_login_id` int(11) NOT NULL,
  `status` varchar(50) NOT NULL,
  `adopted_user_login_id` int(11) NOT NULL,
  `rescue_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_adoption`
--

INSERT INTO `tbl_adoption` (`adoption_id`, `pet_type`, `tag_name`, `breed`, `age`, `gender`, `date`, `photo`, `Ac_login_id`, `status`, `adopted_user_login_id`, `rescue_id`) VALUES
(1, 'Dogs', 'Stella', 'rottwieler', 2, 'Male', '2023-03-02', '/media/34..jpg', 3, 'Adopted', 1, 1),
(2, 'Dogs', 'Kichu', 'Persian', 3, 'Male', '2023-03-04', '/media/35..jpg', 3, 'Not Adopted', 0, 2);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_agency_register`
--

CREATE TABLE `tbl_agency_register` (
  `aid_id` int(11) NOT NULL,
  `login_id` int(11) NOT NULL,
  `agency_name` varchar(50) DEFAULT NULL,
  `phone_number` bigint(20) DEFAULT NULL,
  `address` longtext DEFAULT NULL,
  `mail_id` varchar(50) NOT NULL,
  `place_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_agency_register`
--

INSERT INTO `tbl_agency_register` (`aid_id`, `login_id`, `agency_name`, `phone_number`, `address`, `mail_id`, `place_id`) VALUES
(1, 3, 'Pets Station', 9865321245, 'Pets Villa', 'petss@gmail.com', 1),
(2, 4, 'Pets Care', 9878451285, 'pets ', 'petscare@gmail.com', 1);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_boarding_service`
--

CREATE TABLE `tbl_boarding_service` (
  `b_service_id` int(11) NOT NULL,
  `pet_type` varchar(50) NOT NULL,
  `cost` int(11) NOT NULL,
  `Ac_login_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_boarding_service`
--

INSERT INTO `tbl_boarding_service` (`b_service_id`, `pet_type`, `cost`, `Ac_login_id`) VALUES
(2, 'Dogs', 250, 3),
(3, 'Fish', 1400, 3),
(4, 'Rabbits', 2550, 3);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_booking_boarding`
--

CREATE TABLE `tbl_booking_boarding` (
  `boarding_booking_id` int(11) NOT NULL,
  `starting_date` date NOT NULL,
  `ending_date` date NOT NULL,
  `pet_id` int(11) NOT NULL,
  `b_service_id` int(11) NOT NULL,
  `user_login_id` int(11) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_booking_boarding`
--

INSERT INTO `tbl_booking_boarding` (`boarding_booking_id`, `starting_date`, `ending_date`, `pet_id`, `b_service_id`, `user_login_id`, `status`) VALUES
(1, '2023-03-06', '2023-03-15', 1, 2, 1, 'Accepted');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_booking_grooming`
--

CREATE TABLE `tbl_booking_grooming` (
  `grroming_booking_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `pet_id` int(11) NOT NULL,
  `g_service_id` int(11) NOT NULL,
  `user_login_id` int(11) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_booking_grooming`
--

INSERT INTO `tbl_booking_grooming` (`grroming_booking_id`, `date`, `pet_id`, `g_service_id`, `user_login_id`, `status`) VALUES
(1, '2023-03-14', 1, 1, 1, 'Accepted');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_complaint`
--

CREATE TABLE `tbl_complaint` (
  `complaint_id` int(11) NOT NULL,
  `complaint_subject` varchar(50) NOT NULL,
  `complaint` varchar(150) NOT NULL,
  `user_login_id` int(11) NOT NULL,
  `reply` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_complaint`
--

INSERT INTO `tbl_complaint` (`complaint_id`, `complaint_subject`, `complaint`, `user_login_id`, `reply`) VALUES
(1, 'Save dogs', 'Save stray dogs in kottayam and provide a shelter', 1, 'A Plan to start a shelter in Ktm'),
(2, 'Agressive Dogs are wandering in city', 'pandalam town in pathanamthitta distict in kerala . stray dogs wandering  they are very aggressive and they have no food. ', 1, 'No');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_country`
--

CREATE TABLE `tbl_country` (
  `country_id` int(11) NOT NULL,
  `country` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_country`
--

INSERT INTO `tbl_country` (`country_id`, `country`) VALUES
(1, 'India'),
(2, 'United State of Ameica'),
(3, 'UK');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_district`
--

CREATE TABLE `tbl_district` (
  `district_id` int(11) NOT NULL,
  `district` varchar(50) NOT NULL,
  `state_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_district`
--

INSERT INTO `tbl_district` (`district_id`, `district`, `state_id_id`) VALUES
(1, 'Trivandrum', 1),
(2, 'Pathanamthitta', 1),
(3, 'Ernakulam', 1),
(4, 'Kollam', 1);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_feedback`
--

CREATE TABLE `tbl_feedback` (
  `feedback_id` int(11) NOT NULL,
  `feedback_subject` varchar(50) NOT NULL,
  `feedback` varchar(150) NOT NULL,
  `Ac_login_id` int(11) NOT NULL,
  `user_login_id` int(11) NOT NULL,
  `reply` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_feedback`
--

INSERT INTO `tbl_feedback` (`feedback_id`, `feedback_subject`, `feedback`, `Ac_login_id`, `user_login_id`, `reply`) VALUES
(1, 'Thanks to all of you', 'Thanks for save the dog life', 3, 1, 'No');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_grooming_service`
--

CREATE TABLE `tbl_grooming_service` (
  `g_service_id` int(11) NOT NULL,
  `service_name` varchar(50) NOT NULL,
  `pet_type` varchar(50) NOT NULL,
  `description` longtext NOT NULL,
  `cost` int(11) NOT NULL,
  `Ac_login_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_grooming_service`
--

INSERT INTO `tbl_grooming_service` (`g_service_id`, `service_name`, `pet_type`, `description`, `cost`, `Ac_login_id`) VALUES
(1, 'Essential Package', 'Dogs', 'Bath And Blow Dry, Cleaning Package', 1449, 3),
(2, 'All in one Pack', 'Dogs', 'Bath And Blow Dry,Hair Cut,Cleaning Package,Face and Feet Trim', 2099, 3),
(3, 'Ticks and Flea Controls', 'Dogs', 'Bath And Blow Dry,Anti Tick Treatment', 1500, 3),
(5, 'All in one Packs', 'Cats', 'Bath And Blow Dry,Anti Tick Treatment', 1499, 3),
(6, 'Essential Package', 'Cats', 'Bath And Blow Dry,Anti Tick Treatment', 1900, 3);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_login`
--

CREATE TABLE `tbl_login` (
  `login_id` int(11) NOT NULL,
  `username` varchar(50) DEFAULT NULL,
  `password` longtext DEFAULT NULL,
  `Usertype` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_login`
--

INSERT INTO `tbl_login` (`login_id`, `username`, `password`, `Usertype`, `status`) VALUES
(1, 'anu123', 'anu123', 'User', 'Approved'),
(2, 'jinu123', 'jinu123', 'User', 'Approved'),
(3, 'pets123', 'pets123', 'Adoption Center', 'Approved'),
(4, 'petscare123', 'petscare123', 'Adoption Center', 'Approved'),
(5, 'anut123', 'anut123', 'User', 'Approved');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_pets`
--

CREATE TABLE `tbl_pets` (
  `id` bigint(20) NOT NULL,
  `pname` varchar(50) NOT NULL,
  `breed` varchar(50) NOT NULL,
  `type` varchar(50) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `description` longtext NOT NULL,
  `age` int(11) NOT NULL,
  `image` varchar(50) NOT NULL,
  `user_login_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_pets`
--

INSERT INTO `tbl_pets` (`id`, `pname`, `breed`, `type`, `gender`, `description`, `age`, `image`, `user_login_id`) VALUES
(1, 'Chikku', 'Rotweiler', 'Dogs', 'Male', 'Very Lovable', 3, '/media/28..png', 1),
(2, 'chinnu', 'Persian', 'Cats', 'Female', 'Very Beautiful', 2, '/media/29..jpg', 1);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_place`
--

CREATE TABLE `tbl_place` (
  `place_id` int(11) NOT NULL,
  `place` varchar(50) NOT NULL,
  `district_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_place`
--

INSERT INTO `tbl_place` (`place_id`, `place`, `district_id_id`) VALUES
(1, 'Adoor', 2),
(2, 'Pathanamthitta', 2),
(3, 'Pandalam', 2);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_rescue`
--

CREATE TABLE `tbl_rescue` (
  `rescue_id` int(11) NOT NULL,
  `subject` varchar(50) NOT NULL,
  `description` varchar(150) NOT NULL,
  `date` date NOT NULL,
  `Ac_login_id` int(11) NOT NULL,
  `user_login_id` int(11) NOT NULL,
  `reply` varchar(50) NOT NULL,
  `photo` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_rescue`
--

INSERT INTO `tbl_rescue` (`rescue_id`, `subject`, `description`, `date`, `Ac_login_id`, `user_login_id`, `reply`, `photo`, `status`) VALUES
(1, 'Stray Dog', 'Please Help', '2023-03-03', 3, 1, 'Nil', '/media/30..png', 'User Adoption'),
(2, 'Stray Dog in street', 'Please adopt and save his life', '2023-03-03', 3, 1, 'Nil', '/media/31..jpg', 'User Adoption'),
(3, 'Cat ', 'Please save her', '2023-03-03', 3, 1, 'fgdfg', '/media/32..jpg', 'Adopted to Shelter'),
(4, 'Stray Dog', 'Dogs', '2023-03-03', 3, 1, 'Nil', '/media/33..jpg', 'Submitted');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_state`
--

CREATE TABLE `tbl_state` (
  `state_id` int(11) NOT NULL,
  `state` varchar(50) NOT NULL,
  `country_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_state`
--

INSERT INTO `tbl_state` (`state_id`, `state`, `country_id_id`) VALUES
(1, 'Kerala', 1),
(2, 'Tamil Nadu', 1),
(3, 'Karnataka', 1);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_user_register`
--

CREATE TABLE `tbl_user_register` (
  `user_id` int(11) NOT NULL,
  `login_id` int(11) NOT NULL,
  `firstname` varchar(50) DEFAULT NULL,
  `lastname` varchar(50) DEFAULT NULL,
  `phone_number` bigint(20) DEFAULT NULL,
  `address` longtext DEFAULT NULL,
  `mail_id` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_user_register`
--

INSERT INTO `tbl_user_register` (`user_id`, `login_id`, `firstname`, `lastname`, `phone_number`, `address`, `mail_id`) VALUES
(1, 1, 'Anu', 'Thomas', 9857632514, 'anu Villa', 'anu@gmil.com'),
(2, 2, 'Jinu', 'Tom', 9865321245, 'jinu villa', 'jinu@gmail.com'),
(3, 5, 'Anut', 'Tom', 9865321425, 'anuvilla', 'anut@gmail.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `tbl_adoption`
--
ALTER TABLE `tbl_adoption`
  ADD PRIMARY KEY (`adoption_id`);

--
-- Indexes for table `tbl_agency_register`
--
ALTER TABLE `tbl_agency_register`
  ADD PRIMARY KEY (`aid_id`);

--
-- Indexes for table `tbl_boarding_service`
--
ALTER TABLE `tbl_boarding_service`
  ADD PRIMARY KEY (`b_service_id`);

--
-- Indexes for table `tbl_booking_boarding`
--
ALTER TABLE `tbl_booking_boarding`
  ADD PRIMARY KEY (`boarding_booking_id`);

--
-- Indexes for table `tbl_booking_grooming`
--
ALTER TABLE `tbl_booking_grooming`
  ADD PRIMARY KEY (`grroming_booking_id`);

--
-- Indexes for table `tbl_complaint`
--
ALTER TABLE `tbl_complaint`
  ADD PRIMARY KEY (`complaint_id`);

--
-- Indexes for table `tbl_country`
--
ALTER TABLE `tbl_country`
  ADD PRIMARY KEY (`country_id`);

--
-- Indexes for table `tbl_district`
--
ALTER TABLE `tbl_district`
  ADD PRIMARY KEY (`district_id`),
  ADD KEY `tbl_district_state_id_id_0773a225_fk_tbl_state_state_id` (`state_id_id`);

--
-- Indexes for table `tbl_feedback`
--
ALTER TABLE `tbl_feedback`
  ADD PRIMARY KEY (`feedback_id`);

--
-- Indexes for table `tbl_grooming_service`
--
ALTER TABLE `tbl_grooming_service`
  ADD PRIMARY KEY (`g_service_id`);

--
-- Indexes for table `tbl_login`
--
ALTER TABLE `tbl_login`
  ADD PRIMARY KEY (`login_id`);

--
-- Indexes for table `tbl_pets`
--
ALTER TABLE `tbl_pets`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tbl_place`
--
ALTER TABLE `tbl_place`
  ADD PRIMARY KEY (`place_id`),
  ADD KEY `tbl_place_district_id_id_05c6cb74_fk_tbl_district_district_id` (`district_id_id`);

--
-- Indexes for table `tbl_rescue`
--
ALTER TABLE `tbl_rescue`
  ADD PRIMARY KEY (`rescue_id`);

--
-- Indexes for table `tbl_state`
--
ALTER TABLE `tbl_state`
  ADD PRIMARY KEY (`state_id`),
  ADD KEY `tbl_state_country_id_id_046eec98_fk_tbl_country_country_id` (`country_id_id`);

--
-- Indexes for table `tbl_user_register`
--
ALTER TABLE `tbl_user_register`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=89;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `tbl_adoption`
--
ALTER TABLE `tbl_adoption`
  MODIFY `adoption_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `tbl_agency_register`
--
ALTER TABLE `tbl_agency_register`
  MODIFY `aid_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `tbl_boarding_service`
--
ALTER TABLE `tbl_boarding_service`
  MODIFY `b_service_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `tbl_booking_boarding`
--
ALTER TABLE `tbl_booking_boarding`
  MODIFY `boarding_booking_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tbl_booking_grooming`
--
ALTER TABLE `tbl_booking_grooming`
  MODIFY `grroming_booking_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tbl_complaint`
--
ALTER TABLE `tbl_complaint`
  MODIFY `complaint_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `tbl_country`
--
ALTER TABLE `tbl_country`
  MODIFY `country_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `tbl_district`
--
ALTER TABLE `tbl_district`
  MODIFY `district_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `tbl_feedback`
--
ALTER TABLE `tbl_feedback`
  MODIFY `feedback_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tbl_grooming_service`
--
ALTER TABLE `tbl_grooming_service`
  MODIFY `g_service_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `tbl_login`
--
ALTER TABLE `tbl_login`
  MODIFY `login_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `tbl_pets`
--
ALTER TABLE `tbl_pets`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `tbl_place`
--
ALTER TABLE `tbl_place`
  MODIFY `place_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `tbl_rescue`
--
ALTER TABLE `tbl_rescue`
  MODIFY `rescue_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `tbl_state`
--
ALTER TABLE `tbl_state`
  MODIFY `state_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `tbl_user_register`
--
ALTER TABLE `tbl_user_register`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `tbl_district`
--
ALTER TABLE `tbl_district`
  ADD CONSTRAINT `tbl_district_state_id_id_0773a225_fk_tbl_state_state_id` FOREIGN KEY (`state_id_id`) REFERENCES `tbl_state` (`state_id`);

--
-- Constraints for table `tbl_place`
--
ALTER TABLE `tbl_place`
  ADD CONSTRAINT `tbl_place_district_id_id_05c6cb74_fk_tbl_district_district_id` FOREIGN KEY (`district_id_id`) REFERENCES `tbl_district` (`district_id`);

--
-- Constraints for table `tbl_state`
--
ALTER TABLE `tbl_state`
  ADD CONSTRAINT `tbl_state_country_id_id_046eec98_fk_tbl_country_country_id` FOREIGN KEY (`country_id_id`) REFERENCES `tbl_country` (`country_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
