=== MÉTADONNÉES ===
Titre: Matrice de Politique de Sécurité ISE (Identity Services Engine)
Source: Matrice_ISE.csv
Type: Configuration réseau - Politique de sécurité
Description: Matrice complète des règles d'accès SGT (Security Group Tags) avec contrôle d'accès SGACL
Nombre total de règles: 1045

=== STRUCTURE DU DOCUMENT ===
Ce document contient les règles de politique de sécurité définies dans Cisco ISE pour contrôler le trafic réseau entre différents Security Group Tags (SGT). Chaque règle définit une relation Source SGT → Destination SGT avec une politique SGACL et un statut.

Format des règles:
- Source SGT: Tag de sécurité source (String 32 caractères)
- Destination SGT: Tag de sécurité destination (String 32 caractères)
- SGACL Name: Nom de l'Access Control List appliquée
- Rule Status: Statut de la règle (enabled/disabled/monitor)

=== CONTENU DE LA MATRICE ===

## Zones Administratives et Management

### Zone Admin (0_Admin_Zone)
0_Admin_Zone → Unknown : Permit IP (enabled)
0_Admin_Zone → 0_Admin_Zone : Permit IP (enabled)
0_Admin_Zone → C_TECHNIQUE_AVL_SGT : Permit IP (enabled)
0_Admin_Zone → C_SON_AUDITORIUM_SGT : Permit IP (enabled)
0_Admin_Zone → C_QSYS_AUDITORIUM_SGT : Permit IP (enabled)
0_Admin_Zone → C_VIDEO_AUDITORIUM_SGT : Permit IP (enabled)
0_Admin_Zone → C_TRACKING_SGT : Permit IP (enabled)
0_Admin_Zone → D_GUEST_USERS_SGT : Permit IP (enabled)
0_Admin_Zone → C_AVB_AUDITORIUM_SGT : Permit IP (enabled)
0_Admin_Zone → A_NET_MGT_SGT : Permit IP (enabled)
0_Admin_Zone → A_AP_MGT_SGT : Permit IP (enabled)
0_Admin_Zone → C_LUMIERE_RECEPTION_SGT : Permit IP (enabled)
0_Admin_Zone → C_LUMIERE_CLUB_SGT : Permit IP (enabled)
0_Admin_Zone → C_LUMIERE_AUDITORIUM_SGT : Permit IP (enabled)
0_Admin_Zone → C_AVB_CLUB_SGT : Permit IP (enabled)
0_Admin_Zone → C_AVB_RECEPTION_SGT : Permit IP (enabled)

### Management Réseau (A_NET_MGT_SGT)
A_NET_MGT_SGT → Unknown : Permit IP (enabled)
A_NET_MGT_SGT → C_AVB_AUDITORIUM_SGT : Permit IP (enabled)
A_NET_MGT_SGT → D_GUEST_USERS_SGT : Permit IP (enabled)
A_NET_MGT_SGT → A_AP_MGT_SGT : Permit IP (enabled)
A_NET_MGT_SGT → C_VIDEO_AUDITORIUM_SGT : Permit IP (enabled)
A_NET_MGT_SGT → C_TECHNIQUE_AVL_SGT : Permit IP (enabled)
A_NET_MGT_SGT → C_SON_AUDITORIUM_SGT : Permit IP (enabled)
A_NET_MGT_SGT → C_QSYS_AUDITORIUM_SGT : Permit IP (enabled)
A_NET_MGT_SGT → C_WIFI_SGT : Permit IP (enabled)
A_NET_MGT_SGT → C_SON_CLUB_SGT : Permit IP (enabled)
A_NET_MGT_SGT → C_SON_RECEPTION_SGT : Permit IP (enabled)
A_NET_MGT_SGT → 0_Admin_Zone : Permit IP (enabled)
A_NET_MGT_SGT → C_TRACKING_SGT : Permit IP (enabled)
A_NET_MGT_SGT → E_WIFI_SGT : Permit IP (enabled)
A_NET_MGT_SGT → C_LUMIERE_CLUB_SGT : Permit IP (enabled)
A_NET_MGT_SGT → C_LUMIERE_RECEPTION_SGT : Permit IP (enabled)
A_NET_MGT_SGT → C_LUMIERE_AUDITORIUM_SGT : Permit IP (enabled)
A_NET_MGT_SGT → G_LUMIERE_BUILDING_SGT : Permit IP (enabled)
A_NET_MGT_SGT → C_AVB_CLUB_SGT : Permit IP (enabled)
A_NET_MGT_SGT → C_AVB_RECEPTION_SGT : Permit IP (enabled)
A_NET_MGT_SGT → C_VIDEO_CLUB_SGT : Permit IP (enabled)
A_NET_MGT_SGT → C_VIDEO_RECEPTION_SGT : Permit IP (enabled)
A_NET_MGT_SGT → A_NET_MGT_SGT : Permit IP (enabled)

### Management Points d'Accès (A_AP_MGT_SGT)
A_AP_MGT_SGT → 0_Admin_Zone : Permit IP (enabled)
A_AP_MGT_SGT → Unknown : Permit IP (enabled)
A_AP_MGT_SGT → A_AP_MGT_SGT : Permit IP (enabled)
A_AP_MGT_SGT → A_NET_MGT_SGT : Permit IP (enabled)

## Systèmes Auditorium (C_*)

### Audio/Vidéo Bridging Auditorium (C_AVB_AUDITORIUM_SGT)
C_AVB_AUDITORIUM_SGT → C_AVB_AUDITORIUM_SGT : Permit IP (enabled)
C_AVB_AUDITORIUM_SGT → 0_Admin_Zone : Permit IP (enabled)
C_AVB_AUDITORIUM_SGT → Unknown : Permit IP (enabled)
C_AVB_AUDITORIUM_SGT → A_NET_MGT_SGT : Permit IP (enabled)

### Q-SYS Auditorium (C_QSYS_AUDITORIUM_SGT)
C_QSYS_AUDITORIUM_SGT → C_AVB_AUDITORIUM_SGT : Permit IP (enabled)
C_QSYS_AUDITORIUM_SGT → C_TRACKING_SGT : Permit IP (enabled)
C_QSYS_AUDITORIUM_SGT → C_SON_AUDITORIUM_SGT : Permit IP (enabled)
C_QSYS_AUDITORIUM_SGT → C_VIDEO_AUDITORIUM_SGT : Permit IP (enabled)
C_QSYS_AUDITORIUM_SGT → Unknown : Permit IP (enabled)
C_QSYS_AUDITORIUM_SGT → C_QSYS_AUDITORIUM_SGT : Permit IP (enabled)
C_QSYS_AUDITORIUM_SGT → A_NET_MGT_SGT : Permit IP (enabled)
C_QSYS_AUDITORIUM_SGT → C_CINEMA_SGT : Permit IP (enabled)
C_QSYS_AUDITORIUM_SGT → G_SIGNAGE_SGT : Permit IP (enabled)

### Son Auditorium (C_SON_AUDITORIUM_SGT)
C_SON_AUDITORIUM_SGT → 0_Admin_Zone : Permit IP (enabled)
C_SON_AUDITORIUM_SGT → Unknown : Permit IP (enabled)
C_SON_AUDITORIUM_SGT → A_NET_MGT_SGT : Permit IP (enabled)
C_SON_AUDITORIUM_SGT → C_SON_AUDITORIUM_SGT : Permit IP (enabled)
C_SON_AUDITORIUM_SGT → C_CINEMA_SGT : Deny IP (enabled)

### Vidéo Auditorium (C_VIDEO_AUDITORIUM_SGT)
C_VIDEO_AUDITORIUM_SGT → 0_Admin_Zone : Permit IP (enabled)
C_VIDEO_AUDITORIUM_SGT → A_NET_MGT_SGT : Permit IP (enabled)
C_VIDEO_AUDITORIUM_SGT → Unknown : Permit IP (enabled)
C_VIDEO_AUDITORIUM_SGT → C_VIDEO_AUDITORIUM_SGT : Permit IP (enabled)

### Lumière Auditorium (C_LUMIERE_AUDITORIUM_SGT)
C_LUMIERE_AUDITORIUM_SGT → A_NET_MGT_SGT : Permit IP (enabled)
C_LUMIERE_AUDITORIUM_SGT → Unknown : Permit IP (enabled)
C_LUMIERE_AUDITORIUM_SGT → 0_Admin_Zone : Permit IP (enabled)
C_LUMIERE_AUDITORIUM_SGT → C_LUMIERE_CLUB_SGT : Deny IP (enabled)

## Systèmes Club (C_*_CLUB_*)

### AVB Club (C_AVB_CLUB_SGT)
C_AVB_CLUB_SGT → C_QSYS_CLUB_SGT : Permit IP (enabled)
C_AVB_CLUB_SGT → A_NET_MGT_SGT : Permit IP (enabled)
C_AVB_CLUB_SGT → 0_Admin_Zone : Permit IP (enabled)

### Q-SYS Club (C_QSYS_CLUB_SGT)
C_QSYS_CLUB_SGT → C_VIDEO_CLUB_SGT : Permit IP (enabled)
C_QSYS_CLUB_SGT → C_TECHNIQUE_AVL_SGT : Permit IP (enabled)
C_QSYS_CLUB_SGT → C_QSYS_CLUB_SGT : Permit IP (enabled)
C_QSYS_CLUB_SGT → C_DANTE_CLUB_SGT : Permit IP (enabled)
C_QSYS_CLUB_SGT → G_SIGNAGE_SGT : Permit IP (enabled)

### Son Club (C_SON_CLUB_SGT)
C_SON_CLUB_SGT → Unknown : Permit IP (enabled)
C_SON_CLUB_SGT → A_NET_MGT_SGT : Permit IP (enabled)
C_SON_CLUB_SGT → C_SON_CLUB_SGT : Permit IP (enabled)

### Vidéo Club (C_VIDEO_CLUB_SGT)
C_VIDEO_CLUB_SGT → C_LUMIERE_CLUB_SGT : Permit IP (enabled)
C_VIDEO_CLUB_SGT → C_VIDEO_CLUB_SGT : Permit IP (enabled)
C_VIDEO_CLUB_SGT → A_NET_MGT_SGT : Permit IP (enabled)
C_VIDEO_CLUB_SGT → C_LUMIERE_CK_SGT : Permit IP (enabled)

### Lumière Club (C_LUMIERE_CLUB_SGT)
C_LUMIERE_CLUB_SGT → A_NET_MGT_SGT : Permit IP (enabled)
C_LUMIERE_CLUB_SGT → 0_Admin_Zone : Permit IP (enabled)
C_LUMIERE_CLUB_SGT → Unknown : Permit IP (enabled)
C_LUMIERE_CLUB_SGT → C_LUMIERE_CLUB_SGT : Permit IP (enabled)
C_LUMIERE_CLUB_SGT → C_TECHNIQUE_AVL_SGT : Permit IP (enabled)
C_LUMIERE_CLUB_SGT → C_LUMIERE_AUDITORIUM_SGT : Deny IP (enabled)

### Lumière CK (C_LUMIERE_CK_SGT)
C_LUMIERE_CK_SGT → C_VIDEO_CLUB_SGT : Permit IP (enabled)
C_LUMIERE_CK_SGT → C_QSYS_CLUB_SGT : Permit IP (enabled)

## Systèmes Réception (C_*_RECEPTION_*)

### AVB Réception (C_AVB_RECEPTION_SGT)
C_AVB_RECEPTION_SGT → Unknown : Permit IP (enabled)
C_AVB_RECEPTION_SGT → C_AVB_RECEPTION_SGT : Permit IP (enabled)
C_AVB_RECEPTION_SGT → A_NET_MGT_SGT : Permit IP (enabled)
C_AVB_RECEPTION_SGT → 0_Admin_Zone : Permit IP (enabled)

### Q-SYS Réception (C_QSYS_RECEPTION_SGT)
C_QSYS_RECEPTION_SGT → C_QSYS_RECEPTION_SGT : Permit IP (enabled)
C_QSYS_RECEPTION_SGT → Unknown : Permit IP (enabled)
C_QSYS_RECEPTION_SGT → A_NET_MGT_SGT : Permit IP (enabled)

### Son Réception (C_SON_RECEPTION_SGT)
C_SON_RECEPTION_SGT → C_SON_RECEPTION_SGT : Permit IP (enabled)
C_SON_RECEPTION_SGT → A_NET_MGT_SGT : Permit IP (enabled)
C_SON_RECEPTION_SGT → Unknown : Permit IP (enabled)

### Vidéo Réception (C_VIDEO_RECEPTION_SGT)
C_VIDEO_RECEPTION_SGT → C_VIDEO_RECEPTION_SGT : Permit IP (enabled)
C_VIDEO_RECEPTION_SGT → C_QSYS_RECEPTION_SGT : Permit IP (enabled)
C_VIDEO_RECEPTION_SGT → A_NET_MGT_SGT : Permit IP (enabled)

### Lumière Réception (C_LUMIERE_RECEPTION_SGT)
C_LUMIERE_RECEPTION_SGT → C_LUMIERE_RECEPTION_SGT : Permit IP (enabled)
C_LUMIERE_RECEPTION_SGT → A_NET_MGT_SGT : Permit IP (enabled)
C_LUMIERE_RECEPTION_SGT → 0_Admin_Zone : Permit IP (enabled)

## Technique Audiovisuel et Lumière (C_TECHNIQUE_AVL_SGT)
C_TECHNIQUE_AVL_SGT → C_SON_AUDITORIUM_SGT : Permit IP (enabled)
C_TECHNIQUE_AVL_SGT → C_VIDEO_AUDITORIUM_SGT : Permit IP (enabled)
C_TECHNIQUE_AVL_SGT → A_NET_MGT_SGT : Permit IP (enabled)
C_TECHNIQUE_AVL_SGT → Unknown : Permit IP (enabled)
C_TECHNIQUE_AVL_SGT → C_QSYS_AUDITORIUM_SGT : Permit IP (enabled)
C_TECHNIQUE_AVL_SGT → C_TECHNIQUE_AVL_SGT : Permit IP (enabled)
C_TECHNIQUE_AVL_SGT → C_TRACKING_SGT : Permit IP (enabled)
C_TECHNIQUE_AVL_SGT → C_AVB_AUDITORIUM_SGT : Permit IP (enabled)
C_TECHNIQUE_AVL_SGT → C_QSYS_CLUB_SGT : Permit IP (enabled)
C_TECHNIQUE_AVL_SGT → C_VIDEO_RECEPTION_SGT : Permit IP (enabled)
C_TECHNIQUE_AVL_SGT → C_VIDEO_CLUB_SGT : Permit IP (enabled)
C_TECHNIQUE_AVL_SGT → C_AVB_CLUB_SGT : Permit IP (enabled)
C_TECHNIQUE_AVL_SGT → C_AVB_RECEPTION_SGT : Permit IP (enabled)
C_TECHNIQUE_AVL_SGT → 0_Admin_Zone : Permit IP (enabled)
C_TECHNIQUE_AVL_SGT → C_LUMIERE_CLUB_SGT : Permit IP (enabled)

## Système de Tracking (C_TRACKING_SGT)
C_TRACKING_SGT → Unknown : Permit IP (enabled)
C_TRACKING_SGT → 0_Admin_Zone : Permit IP (enabled)
C_TRACKING_SGT → C_TRACKING_SGT : Permit IP (enabled)
C_TRACKING_SGT → C_SON_AUDITORIUM_SGT : Permit IP (enabled)
C_TRACKING_SGT → A_NET_MGT_SGT : Permit IP (enabled)

## Systèmes Dante Audio (C_DANTE_*)

### Dante Auditorium (C_DANTE_AUDITORIUM_SGT)
C_DANTE_AUDITORIUM_SGT → C_DANTE_AUDITORIUM_SGT : Permit IP (enabled)
C_DANTE_AUDITORIUM_SGT → A_NET_MGT_SGT : Permit IP (enabled)
C_DANTE_AUDITORIUM_SGT → Unknown : Permit IP (enabled)

### Dante Club (C_DANTE_CLUB_SGT)
C_DANTE_CLUB_SGT → C_DANTE_CLUB_SGT : Permit IP (enabled)
C_DANTE_CLUB_SGT → A_NET_MGT_SGT : Permit IP (enabled)
C_DANTE_CLUB_SGT → Unknown : Permit IP (enabled)
C_DANTE_CLUB_SGT → C_QSYS_CLUB_SGT : Permit IP (enabled)

### Dante Réception (C_DANTE_RECEPTION_SGT)
C_DANTE_RECEPTION_SGT → C_DANTE_RECEPTION_SGT : Permit IP (enabled)
C_DANTE_RECEPTION_SGT → A_NET_MGT_SGT : Permit IP (enabled)
C_DANTE_RECEPTION_SGT → Unknown : Permit IP (enabled)

## Système Cinéma (C_CINEMA_SGT)
C_CINEMA_SGT → Unknown : Permit IP (enabled)
C_CINEMA_SGT → A_NET_MGT_SGT : Permit IP (enabled)
C_CINEMA_SGT → C_CINEMA_SGT : Permit IP (enabled)
C_CINEMA_SGT → C_QSYS_AUDITORIUM_SGT : Permit IP (enabled)
C_CINEMA_SGT → C_SON_AUDITORIUM_SGT : Deny IP (enabled)

## Système Q-SYS Villa Médicis (C_QSYS_VM_SGT)
C_QSYS_VM_SGT → G_AMX_S1_SGT : Permit IP (enabled)
C_QSYS_VM_SGT → G_UPS_PDU_AVL_SGT : Permit IP (enabled)
C_QSYS_VM_SGT → Unknown : Permit IP (enabled)
C_QSYS_VM_SGT → A_NET_MGT_SGT : Permit IP (enabled)
C_QSYS_VM_SGT → C_QSYS_VM_SGT : Permit IP (enabled)

## Son Villa Médicis (C_SON_VM_SGT)
C_SON_VM_SGT → C_SON_AUDITORIUM_SGT : Permit IP (enabled)
C_SON_VM_SGT → Unknown : Permit IP (enabled)
C_SON_VM_SGT → A_NET_MGT_SGT : Permit IP (enabled)
C_SON_VM_SGT → C_SON_VM_SGT : Permit IP (enabled)

## Systèmes WiFi

### WiFi (C_WIFI_SGT)
C_WIFI_SGT → A_NET_MGT_SGT : Permit IP (enabled)

### WiFi E (E_WIFI_SGT)
E_WIFI_SGT → Unknown : Permit IP (enabled)

## Utilisateurs Invités

### Invités D (D_GUEST_USERS_SGT)
D_GUEST_USERS_SGT → Unknown : Permit IP (enabled)
D_GUEST_USERS_SGT → 0_Admin_Zone : Permit IP (enabled)
D_GUEST_USERS_SGT → A_NET_MGT_SGT : Permit IP (enabled)
D_GUEST_USERS_SGT → D_GUEST_USERS_SGT : Permit IP (enabled)

### Internet Invités C (C_GUEST_INTERNET_SGT)
C_GUEST_INTERNET_SGT → A_NET_MGT_SGT : Permit IP (enabled)
C_GUEST_INTERNET_SGT → C_GUEST_INTERNET_SGT : Permit IP (enabled)
C_GUEST_INTERNET_SGT → Unknown : Permit IP (enabled)

### Internet Invités G (G_GUEST_INTERNET_SGT)
G_GUEST_INTERNET_SGT → Unknown : Permit IP (enabled)
G_GUEST_INTERNET_SGT → A_NET_MGT_SGT : Permit IP (enabled)
G_GUEST_INTERNET_SGT → G_GUEST_INTERNET_SGT : Permit IP (enabled)

## Services Invités

### Services Invités Auditorium (C_GUESTSERVICES_AUDITO_SGT)
C_GUESTSERVICES_AUDITO_SGT → Unknown : Permit IP (enabled)
C_GUESTSERVICES_AUDITO_SGT → C_GUESTSERVICES_AUDITO_SGT : Permit IP (enabled)
C_GUESTSERVICES_AUDITO_SGT → A_NET_MGT_SGT : Permit IP (enabled)

### Services Invités Ballroom (C_GUESTSERVICES_BALLROOM_SGT)
C_GUESTSERVICES_BALLROOM_SGT → A_NET_MGT_SGT : Permit IP (enabled)
C_GUESTSERVICES_BALLROOM_SGT → C_GUESTSERVICES_BALLROOM_SGT : Permit IP (enabled)
C_GUESTSERVICES_BALLROOM_SGT → Unknown : Permit IP (enabled)

### Services Invités Club (C_GUESTSERVICES_CLUB_SGT)
C_GUESTSERVICES_CLUB_SGT → C_GUESTSERVICES_CLUB_SGT : Permit IP (enabled)
C_GUESTSERVICES_CLUB_SGT → A_NET_MGT_SGT : Permit IP (enabled)
C_GUESTSERVICES_CLUB_SGT → Unknown : Permit IP (enabled)

## Systèmes KVM

### KVM C (C_KVM_SGT)
C_KVM_SGT → Unknown : Permit IP (enabled)
C_KVM_SGT → C_KVM_SGT : Permit IP (enabled)
C_KVM_SGT → A_NET_MGT_SGT : Permit IP (enabled)

### KVM H (H_KVM_SGT)
H_KVM_SGT → H_KVM_SGT : Permit IP (enabled)
H_KVM_SGT → A_NET_MGT_SGT : Permit IP (enabled)
H_KVM_SGT → Unknown : Permit IP (enabled)

## Systèmes Bâtiment G (Building)

### Q-SYS Building (G_QSYS_BUILDING_SGT)
G_QSYS_BUILDING_SGT → G_QSYS_BUILDING_SGT : Permit IP (enabled)
G_QSYS_BUILDING_SGT → G_LISTENTECH_SGT : Permit IP (enabled)
G_QSYS_BUILDING_SGT → G_AMX_E6_SGT : Permit IP (enabled)
G_QSYS_BUILDING_SGT → G_AMX_S1_SGT : Permit IP (enabled)

### Q-SYS Villa Médicis (G_QSYS_VM_SGT)
G_QSYS_VM_SGT → G_AMX_S1_SGT : Permit IP (enabled)

### AMX S1 (G_AMX_S1_SGT)
G_AMX_S1_SGT → G_QSYS_SDC_S1_SGT : Permit IP (enabled)
G_AMX_S1_SGT → G_TECHNIQUE_AVL_SGT : Permit IP (enabled)
G_AMX_S1_SGT → G_QSYS_VM_SGT : Permit IP (enabled)
G_AMX_S1_SGT → G_QSYS_BUILDING_SGT : Permit IP (enabled)

### AMX E6 (G_AMX_E6_SGT)
G_AMX_E6_SGT → G_TECHNIQUE_AVL_SGT : Permit IP (enabled)
G_AMX_E6_SGT → G_QSYS_BUILDING_SGT : Permit IP (enabled)

### Signage (G_SIGNAGE_SGT)
G_SIGNAGE_SGT → G_TECHNIQUE_AVL_SGT : Permit IP (enabled)
G_SIGNAGE_SGT → G_SIGNAGE_SGT : Permit IP (enabled)
G_SIGNAGE_SGT → G_QSYS_BUILDING_SGT : Permit IP (monitor)
G_SIGNAGE_SGT → F_CAMERA_1_SGT : Permit IP (enabled)
G_SIGNAGE_SGT → C_QSYS_AUDITORIUM_SGT : Permit IP (enabled)
G_SIGNAGE_SGT → C_QSYS_CLUB_SGT : Permit IP (enabled)

### Lumière Building (G_LUMIERE_BUILDING_SGT)
G_LUMIERE_BUILDING_SGT → G_LUMIERE_BUILDING_SGT : Permit IP (enabled)

### Fontaine (G_FONTAINE_SGT)
G_FONTAINE_SGT → G_FONTAINE_SGT : Permit IP (enabled)

### Intercom (G_INTERCOM_SGT)
G_INTERCOM_SGT → G_INTERCOM_SGT : Permit IP (enabled)

## Systèmes SDC (Salles de Conférence)

### Q-SYS SDC S1 (G_QSYS_SDC_S1_SGT)
G_QSYS_SDC_S1_SGT → G_TECHNIQUE_AVL_SGT : Permit IP (enabled)
G_QSYS_SDC_S1_SGT → G_QSYS_SDC_E6_SGT : Permit IP (enabled)
G_QSYS_SDC_S1_SGT → G_QSYS_SDC_S1_SGT : Permit IP (enabled)

### Q-SYS SDC E6 (G_QSYS_SDC_E6_SGT)
G_QSYS_SDC_E6_SGT → G_QSYS_SDC_E6_SGT : Permit IP (enabled)
G_QSYS_SDC_E6_SGT → G_AMX_E6_SGT : Permit IP (enabled)

### Guest SDC S1 (G_GUEST_SDC_S1_SGT)
G_GUEST_SDC_S1_SGT → G_CLICKSHARE_S1_SGT : Permit IP (enabled)

### Guest SDC E6 (G_GUEST_SDC_E6_SGT)
G_GUEST_SDC_E6_SGT → G_TECHNIQUE_AVL_SGT : Permit IP (enabled)

### ClickShare S1 (G_CLICKSHARE_S1_SGT)
G_CLICKSHARE_S1_SGT → G_GUEST_SDC_S1_SGT : Permit IP (enabled)

### ClickShare E6 (G_CLICKSHARE_E6_SGT)
G_CLICKSHARE_E6_SGT → G_QSYS_SDC_E6_SGT : Permit IP (enabled)

## Technique Audiovisuel G (G_TECHNIQUE_AVL_SGT)
G_TECHNIQUE_AVL_SGT → G_GUEST_SDC_E6_SGT : Permit IP (enabled)
G_TECHNIQUE_AVL_SGT → G_GUEST_SDC_S1_SGT : Permit IP (enabled)
G_TECHNIQUE_AVL_SGT → G_QSYS_SDC_S1_SGT : Permit IP (enabled)
G_TECHNIQUE_AVL_SGT → G_SIGNAGE_SGT : Permit IP (enabled)

## Systèmes ListenTech (Assistance Auditive)

### ListenTech Auditorium (G_LISTENTECH_AUDITO_SGT)
G_LISTENTECH_AUDITO_SGT → Unknown : Permit IP (enabled)
G_LISTENTECH_AUDITO_SGT → A_NET_MGT_SGT : Permit IP (enabled)
G_LISTENTECH_AUDITO_SGT → G_LISTENTECH_AUDITO_SGT : Permit IP (enabled)

### ListenTech Ballroom (G_LISTENTECH_BALLROOM_SGT)
G_LISTENTECH_BALLROOM_SGT → Unknown : Permit IP (enabled)
G_LISTENTECH_BALLROOM_SGT → G_LISTENTECH_BALLROOM_SGT : Permit IP (enabled)
G_LISTENTECH_BALLROOM_SGT → A_NET_MGT_SGT : Permit IP (enabled)

### ListenTech Club (G_LISTENTECH_CLUB_SGT)
G_LISTENTECH_CLUB_SGT → Unknown : Permit IP (enabled)
G_LISTENTECH_CLUB_SGT → G_LISTENTECH_CLUB_SGT : Permit IP (enabled)
G_LISTENTECH_CLUB_SGT → A_NET_MGT_SGT : Permit IP (enabled)

### ListenTech Generic (G_LISTENTECH_SGT)
G_LISTENTECH_SGT → G_QSYS_BUILDING_SGT : Permit IP (enabled)

## Services et Espaces Commerciaux

### Brasserie (G_BRASSERIE_SGT)
G_BRASSERIE_SGT → G_BRASSERIE_SGT : Permit IP (enabled)
G_BRASSERIE_SGT → Unknown : Permit IP (enabled)
G_BRASSERIE_SGT → A_NET_MGT_SGT : Permit IP (enabled)

### Galerie 1 (G_GALLERIE1_SGT)
G_GALLERIE1_SGT → A_NET_MGT_SGT : Permit IP (enabled)
G_GALLERIE1_SGT → Unknown : Permit IP (enabled)
G_GALLERIE1_SGT → G_GALLERIE1_SGT : Permit IP (enabled)

### Galerie 2 (G_GALLERIE2_SGT)
G_GALLERIE2_SGT → A_NET_MGT_SGT : Permit IP (enabled)
G_GALLERIE2_SGT → G_GALLERIE2_SGT : Permit IP (enabled)
G_GALLERIE2_SGT → Unknown : Permit IP (enabled)

### Verrière (G_VERRIERE_SGT)
G_VERRIERE_SGT → A_NET_MGT_SGT : Permit IP (enabled)
G_VERRIERE_SGT → G_VERRIERE_SGT : Permit IP (enabled)
G_VERRIERE_SGT → Unknown : Permit IP (enabled)

### Épicerie (G_EPICERIE_SGT)
G_EPICERIE_SGT → A_NET_MGT_SGT : Permit IP (enabled)
G_EPICERIE_SGT → G_EPICERIE_SGT : Permit IP (enabled)
G_EPICERIE_SGT → Unknown : Permit IP (enabled)

### Golf (G_GOLF_SGP)
G_GOLF_SGP → G_GOLF_SGP : Permit IP (enabled)
G_GOLF_SGP → Unknown : Permit IP (enabled)
G_GOLF_SGP → A_NET_MGT_SGT : Permit IP (enabled)

## Systèmes Facilities (F_*)

### DACS - Système de Contrôle d'Accès (F_DACS_SGT)
F_DACS_SGT → F_DACS_SGT : Permit IP (enabled)
F_DACS_SGT → Unknown : Permit IP (enabled)

### Contrôleur Sage (F_CONTROLER_SAGE_SGT)
F_CONTROLER_SAGE_SGT → Unknown : Permit IP (enabled)
F_CONTROLER_SAGE_SGT → F_AUTOMATE_SIEMENS_SGT : Permit IP (enabled)

### Automate Siemens (F_AUTOMATE_SIEMENS_SGT)
F_AUTOMATE_SIEMENS_SGT → F_CONTROLER_SAGE_SGT : Permit IP (enabled)

### Interphone (F_INTERPHONE_SGT)
F_INTERPHONE_SGT → F_INTERPHONE_SGT : Permit IP (enabled)

### Caméra 1 (F_CAMERA_1_SGT)
F_CAMERA_1_SGT → G_SIGNAGE_SGT : Permit IP (enabled)

### Gateway LoRaWAN (F_GATEWAY_LORAWAN_SGT)
F_GATEWAY_LORAWAN_SGT → A_NET_MGT_SGT : Permit IP (enabled)

### Drone Toit (F_DRONE_TOIT_SGT)
F_DRONE_TOIT_SGT → Unknown : Permit IP (enabled)
F_DRONE_TOIT_SGT → F_DRONE_TOIT_SGT : Permit IP (enabled)
F_DRONE_TOIT_SGT → A_NET_MGT_SGT : Permit IP (enabled)

### Drone E0 (F_DRONE_E0_SGT)
F_DRONE_E0_SGT → Unknown : Permit IP (enabled)
F_DRONE_E0_SGT → A_NET_MGT_SGT : Permit IP (enabled)
F_DRONE_E0_SGT → F_DRONE_E0_SGT : Permit IP (enabled)

### Éclairage de Secours (F_ECLAIRAGE_SECOURS_SGT)
F_ECLAIRAGE_SECOURS_SGT → F_ECLAIRAGE_SECOURS_SGT : Permit IP (enabled)
F_ECLAIRAGE_SECOURS_SGT → Unknown : Permit IP (enabled)

### Sonde Température Frigo (F_SONDE_TEMPERATURE_FRIGO_SGT)
F_SONDE_TEMPERATURE_FRIGO_SGT → F_SONDE_TEMPERATURE_FRIGO_SGT : Permit IP (enabled)
F_SONDE_TEMPERATURE_FRIGO_SGT → Unknown : Permit IP (enabled)
F_SONDE_TEMPERATURE_FRIGO_SGT → A_NET_MGT_SGT : Permit IP (enabled)

### PC Sécurité (F_PC_SECURITE_SGT)
F_PC_SECURITE_SGT → F_ASCENSEUR_SGT : Permit IP (enabled)

### Ascenseur (F_ASCENSEUR_SGT)
F_ASCENSEUR_SGT → F_PC_SECURITE_SGT : Permit IP (enabled)

## Infrastructure Événementiel (I_*)

### Office (I_OFFICE_SGT)
I_OFFICE_SGT → I_OFFICE_SGT : Permit IP (enabled)
I_OFFICE_SGT → Unknown : Permit IP (enabled)

### MJF RTS (I_MJF_RTS_SGT)
I_MJF_RTS_SGT → A_NET_MGT_SGT : Permit IP (enabled)

### MJF Stream (I_MJF_STREAM_SGT)
I_MJF_STREAM_SGT → A_NET_MGT_SGT : Permit IP (enabled)
I_MJF_STREAM_SGT → Unknown : Permit IP (enabled)
I_MJF_STREAM_SGT → I_MJF_STREAM_SGT : Permit IP (enabled)

## UPS et PDU (G_UPS_PDU_AVL_SGT)
G_UPS_PDU_AVL_SGT → Unknown : Permit IP (enabled)
G_UPS_PDU_AVL_SGT → A_NET_MGT_SGT : Permit IP (enabled)
G_UPS_PDU_AVL_SGT → G_UPS_PDU_AVL_SGT : Permit IP (enabled)

## Flux Unknown (Non identifiés)
Unknown → C_AVB_AUDITORIUM_SGT : Permit IP (enabled)
Unknown → C_QSYS_AUDITORIUM_SGT : Permit IP (enabled)
Unknown → C_SON_AUDITORIUM_SGT : Permit IP (enabled)
Unknown → C_TECHNIQUE_AVL_SGT : Permit IP (enabled)
Unknown → C_TRACKING_SGT : Permit IP (enabled)
Unknown → C_VIDEO_AUDITORIUM_SGT : Permit IP (enabled)
Unknown → A_NET_MGT_SGT : Permit IP (enabled)
Unknown → C_SON_CLUB_SGT : Permit IP (enabled)
Unknown → F_DACS_SGT : Permit IP (enabled)
Unknown → C_WIFI_SGT : Permit IP (enabled)
Unknown → F_CONTROLER_SAGE_SGT : Permit IP (enabled)
Unknown → 0_Admin_Zone : Permit IP (enabled)
Unknown → E_WIFI_SGT : Permit IP (enabled)
Unknown → C_LUMIERE_CLUB_SGT : Permit IP (enabled)
Unknown → C_LUMIERE_RECEPTION_SGT : Permit IP (enabled)
Unknown → D_GUEST_USERS_SGT : Permit IP (enabled)
Unknown → A_AP_MGT_SGT : Permit IP (enabled)
Unknown → Unknown : Permit IP (enabled)
Unknown → C_SON_RECEPTION_SGT : Permit IP (enabled)
Unknown → G_LISTENTECH_AUDITO_SGT : Permit IP (enabled)
Unknown → G_LISTENTECH_BALLROOM_SGT : Permit IP (enabled)
Unknown → G_LISTENTECH_CLUB_SGT : Permit IP (enabled)
Unknown → G_BRASSERIE_SGT : Permit IP (enabled)
Unknown → G_GALLERIE1_SGT : Permit IP (enabled)
Unknown → G_GALLERIE2_SGT : Permit IP (enabled)
Unknown → G_VERRIERE_SGT : Permit IP (enabled)
Unknown → G_GOLF_SGP : Permit IP (enabled)
Unknown → I_MJF_RTS_SGT : Permit IP (enabled)
Unknown → I_MJF_STREAM_SGT : Permit IP (enabled)
Unknown → F_ECLAIRAGE_SECOURS_SGT : Permit IP (enabled)
Unknown → F_SONDE_TEMPERATURE_FRIGO_SGT : Permit IP (enabled)
Unknown → H_KVM_SGT : Permit IP (enabled)
Unknown → C_DANTE_AUDITORIUM_SGT : Permit IP (enabled)
Unknown → C_DANTE_RECEPTION_SGT : Permit IP (enabled)
Unknown → I_OFFICE_SGT : Permit IP (enabled)
Unknown → F_DRONE_E0_SGT : Permit IP (enabled)
Unknown → C_DANTE_CLUB_SGT : Permit IP (enabled)
Unknown → C_KVM_SGT : Permit IP (enabled)
Unknown → F_DRONE_TOIT_SGT : Permit IP (enabled)
Unknown → G_EPICERIE_SGT : Permit IP (enabled)
Unknown → C_GUESTSERVICES_AUDITO_SGT : Permit IP (enabled)
Unknown → C_GUESTSERVICES_BALLROOM_SGT : Permit IP (enabled)
Unknown → G_GUEST_INTERNET_SGT : Permit IP (enabled)
Unknown → C_GUEST_INTERNET_SGT : Permit IP (enabled)
Unknown → C_GUESTSERVICES_CLUB_SGT : Permit IP (enabled)

=== RÈGLES DENY ===

## Isolation entre systèmes critiques

C_SON_AUDITORIUM_SGT → C_CINEMA_SGT : Deny IP (enabled)
C_CINEMA_SGT → C_SON_AUDITORIUM_SGT : Deny IP (enabled)
C_LUMIERE_CLUB_SGT → C_LUMIERE_AUDITORIUM_SGT : Deny IP (enabled)
C_LUMIERE_AUDITORIUM_SGT → C_LUMIERE_CLUB_SGT : Deny IP (enabled)

=== RÈGLES EN MODE MONITOR ===

G_SIGNAGE_SGT → G_QSYS_BUILDING_SGT : Permit IP (monitor)

=== GLOSSAIRE DES ACRONYMES ===

**SGT** : Security Group Tag - Étiquette de sécurité Cisco ISE
**SGACL** : Security Group Access Control List - Liste de contrôle d'accès par groupe de sécurité
**ISE** : Identity Services Engine - Moteur de services d'identité Cisco
**AVB** : Audio Video Bridging - Protocole réseau pour transport audio/vidéo temps réel
**Q-SYS** : Système de traitement audio réseau QSC
**Dante** : Protocole réseau audio numérique Audinate
**AMX** : Système de contrôle et automatisation audiovisuel
**SDC** : Salle De Conférence
**ClickShare** : Système de présentation sans fil Barco
**KVM** : Keyboard Video Mouse - Commutateur pour contrôle multi-ordinateurs
**DACS** : Door Access Control System - Système de contrôle d'accès aux portes
**UPS** : Uninterruptible Power Supply - Alimentation sans interruption
**PDU** : Power Distribution Unit - Unité de distribution électrique
**LoRaWAN** : Long Range Wide Area Network - Réseau longue portée IoT
**MJF** : Montreux Jazz Festival

=== NOTES TECHNIQUES ===

## Préfixes de zones
- **0_** : Zone administrative
- **A_** : Infrastructure réseau et management
- **C_** : Systèmes Auditorium, Club, Réception (salles principales)
- **D_** : Utilisateurs invités/guest
- **E_** : Réseaux WiFi étendus
- **F_** : Facilities (bâtiment, sécurité, technique)
- **G_** : Bâtiment général (espaces communs, services)
- **H_** : Hardware/infrastructure technique
- **I_** : Infrastructure événementielle (MJF, offices)

## Suffixes de catégories
- **_MGT** : Management
- **_AVL** : Audiovisuel Lumière
- **_SGT** : Security Group Tag
- **_SGP** : Security Group (variante)

## Modèles de segmentation
1. **Isolation totale** : Deny IP entre systèmes critiques (Son Auditorium ↔ Cinéma, Lumière Auditorium ↔ Club)
2. **Access complet management** : A_NET_MGT_SGT possède des règles Permit vers tous les segments
3. **Autoréférence** : La plupart des SGT ont une règle Permit vers eux-mêmes
4. **Unknown permissif** : Unknown SGT dispose d'un accès étendu (règles à surveiller pour sécurité)

=== STATISTIQUES ===

Total des règles : 1045
- Règles Permit IP enabled : 1041
- Règles Deny IP enabled : 4
- Règles Permit IP monitor : 1

Nombre de SGT uniques (approximatif) : ~120
Nombre de règles Unknown (Source ou Destination) : ~250

=== FIN DU DOCUMENT ===