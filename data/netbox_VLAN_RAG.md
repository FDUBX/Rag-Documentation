=== MÉTADONNÉES ===
Titre: Configuration VLANs NetBox - Millennium Center SA
Source: netbox_VLAN.csv
Type: Documentation infrastructure réseau
Site: Millennium
Entité: Millennium Center SA
Date extraction: 2024-11-10
=== GLOSSAIRE ===
VID: VLAN Identifier (identifiant numérique du VLAN)
VRF: Virtual Routing and Forwarding (instance de routage virtuel)
VLAN: Virtual Local Area Network (réseau local virtuel)
AVB: Audio Video Bridging (protocole réseau audio/vidéo)
AVL: Audiovisuel
Dante: Protocole réseau audio numérique
Q-SYS: Système de traitement audio/vidéo
AP: Access Point (point d'accès WiFi)
WLC: Wireless LAN Controller (contrôleur WiFi)
PnP: Plug and Play
iSCSI: Internet Small Computer System Interface (protocole de stockage)
NFS: Network File System (système de fichiers réseau)
SBC: Session Border Controller (contrôleur de session VoIP)
DMZ: Zone démilitarisée (zone de sécurité réseau)
HA: High Availability (haute disponibilité)
MJF: Montreux Jazz Festival
MAM: Media Asset Management
S3: Simple Storage Service (protocole de stockage objet)
=== CONTENU ===

## VRF A - Infrastructure Management (10.128.0.0/16)

### VLANs de management réseau

VLAN 1 - Default
- Préfixes: 10.132.12.0/24, 10.135.0.0/16
- Description: VLAN de défaut
- ID interne: 74

VLAN 2 - A_NET_MGMT
- Préfixe: 10.128.2.0/24
- Description: VLAN pour le management des équipements
- ID interne: 4

VLAN 4 - A_ADMIN_SRV
- Préfixe: 10.128.4.0/24
- Description: VLAN pour le management des serveurs
- ID interne: 5

VLAN 6 - A_AP_MGT
- Préfixe: 10.128.6.0/24
- Description: VLAN pour le management des access points
- ID interne: 6

VLAN 8 - A_WLC_MGT
- Préfixe: 10.128.8.0/24
- Description: VLAN pour le management des contrôleur Wifi
- ID interne: 7

VLAN 10 - A_PnP
- Préfixe: 10.128.10.0/24
- Description: VLAN pour le service Plug and Play Cisco
- ID interne: 8

### VLANs de management par distribution

VLAN 20 - A_NET_MGT_1
- Préfixe: 10.128.20.0/24
- Description: VLAN pour le management des switch sur distrib étage
- ID interne: 93

VLAN 22 - A_NET_MGT_2
- Préfixe: 10.128.22.0/24
- Description: VLAN pour le management des switch sur distrib AVL
- ID interne: 94

VLAN 24 - A_NET_MGT_3
- Préfixe: 10.128.24.0/24
- Description: VLAN pour le management des switch sur distrib outdoor
- ID interne: 95

VLAN 30 - A_AP_MGT_1
- Préfixe: 10.128.30.0/23
- Description: VLAN pour le management des AP sur distri étage
- ID interne: 90

VLAN 32 - A_AP_MGT_2
- Préfixe: 10.128.32.0/24
- Description: VLAN pour le management des AP sur distri AVL
- ID interne: 91

VLAN 34 - A_AP_MGT_3
- Préfixe: 10.128.34.0/24
- Description: VLAN pour le management des AP sur distri Outdoor
- ID interne: 92

### VLANs de services infrastructure

VLAN 250 - A_FLASHBLADE
- Préfixe: 10.128.250.0/24
- Description: VLAN pour les services fournit par la FlashBlade
- ID interne: 9

VLAN 252 - DNAC Cluster
- Préfixe: 10.128.252.0/30
- Description: VLAN pour la communication du cluster DNAC
- ID interne: 10

### VLANs d'interconnexion VRF A

VLAN 253 - A_Interco Core - Nexus
- Préfixe: 10.128.253.0/30
- Description: VLAN pour l'interconnexion entre les switch Core et Nexus
- ID interne: 11

VLAN 254 - A_Interco Core - Distr
- Préfixe: 10.128.254.0/30
- Description: VLAN pour l'interconnexion entre les switch Core et Distribution
- ID interne: 12

VLAN 255 - A_Interco Core - Fw
- Préfixe: 10.128.255.0/24
- Description: VLAN pour l'interconnexion entre les switch Core et des Firewall
- ID interne: 13

## VRF B - Infrastructure IT & Serveurs (10.129.0.0/16)

### VLANs serveurs et applications

VLAN 258 - B_SERVER
- Préfixe: 10.129.2.0/24
- Description: VLAN pour les serveurs d'infrastructure informatique
- ID interne: 3

VLAN 260 - B_K8s_CLUSTER
- Préfixe: 10.129.4.0/24
- Description: VLAN pour le cluster Kubernetes
- ID interne: 75

VLAN 262 - B_PRE_PROD
- Préfixe: 10.129.6.0/24
- Description: Vlan pour les serveurs de Pre Prod (datacenter)
- ID interne: 109

VLAN 264 - B_ADMIN_ACCESS
- Préfixe: 10.129.8.0/24
- Description: VLAN pour les accès filaires des administrateurs IT
- ID interne: 110

VLAN 266 - B_VCENTER_HA
- Préfixe: 10.129.10.0/24
- Description: VLAN pour le service HA du vCenter
- ID interne: 138

### VLANs téléphonie

VLAN 268 - B_SBC_SRV
- Préfixe: 10.129.12.0/24
- Description: VLAN pour connecter les SBC au réseau téléphonique
- ID interne: 140

VLAN 270 - B_GW_PHONE
- Préfixe: 10.129.14.0/24
- Description: VLAN pour connecter les routeur swisscom au réseau Millennium
- ID interne: 141

VLAN 272 - B_SBC_HA_SRV
- Préfixe: 10.129.16.0/24
- Description: VLAN pour connecter les liens HA des SBC
- ID interne: 145

### VLANs stockage et virtualisation

VLAN 276 - B_iSCSI 1
- Préfixe: 10.129.20.0/24
- Description: VLAN pour le service iSCSI
- ID interne: 14

VLAN 278 - B_iSCSI 2
- Préfixe: 10.129.22.0/24
- Description: VLAN pour le service iSCSI
- ID interne: 15

VLAN 280 - B_vMotion
- Préfixe: 10.129.24.0/24
- Description: VLAN pour le service vMotion sur vCenter
- ID interne: 16

VLAN 282 - B_NFS
- Préfixe: 10.129.26.0/24
- Description: VLAN pour le service NFS
- ID interne: 17

### VLANs utilisateurs

VLAN 448 - B_WIFI
- Préfixe: 10.129.192.0/24
- Description: VLAN pour l'accès WIFI
- ID interne: 100
- Étiquettes: WIFI

### VLANs services infrastructure VRF B

VLAN 506 - B_FLASHBLADE
- Préfixe: 10.129.250.0/24
- Description: VLAN pour les services fournit par la FlashBlade
- ID interne: 18

### VLANs d'interconnexion VRF B

VLAN 509 - B_Interco Core - Nexus
- Préfixe: 10.129.253.0/30
- Description: VLAN pour l'interconnexion entre les switch Core et Nexus
- ID interne: 19

VLAN 510 - B_Interco Core - Distr
- Préfixe: 10.129.254.0/30
- Description: VLAN pour l'interconnexion entre les switch Core et Distribution
- ID interne: 20

VLAN 511 - B_Interco Core - Fw
- Préfixe: 10.129.255.0/30
- Description: VLAN pour l'interconnexion entre les switch Core et des Firewall
- ID interne: 21

## VRF C - Audiovisuel Production (10.130.0.0/16)

### VLANs audio réseau

VLAN 512 - C_AVB_AUDITORIUM
- Préfixe: 10.130.0.0/24
- Description: VLAN pour le protocole AVB de la zone Auditorium
- ID interne: 185

VLAN 514 - C_AVB
- Préfixe: 10.130.2.0/24
- Description: VLAN pour les services AVB
- ID interne: 22

VLAN 524 - C_AVB_CLUB
- Préfixe: 10.130.4.0/24
- ID interne: 191

VLAN 534 - C_QSYS
- Préfixe: 10.130.22.0/24
- Description: VLAN pour le système QSYS
- ID interne: 32

VLAN 536 - C_SON
- Préfixe: 10.130.24.0/23
- Description: VLAN pour le service de sonorisation
- ID interne: 33

VLAN 538 - C_DANTE_AUDITORIUM
- Préfixe: 10.130.26.0/24
- Description: VLAN pour le service de sonorisation de l'auditorium
- ID interne: 209

VLAN 540 - C_DANTE_CLUB
- Préfixe: 10.130.28.0/24
- Description: VLAN pour le service de sonorisation du club
- ID interne: 177

VLAN 542 - C_DANTE_STRAV
- Préfixe: 10.130.30.0/24
- Description: VLAN pour le service de sonorisation du Stravinsky
- ID interne: 210

VLAN 544 - C_DANTE_TERRASSES
- Préfixe: 10.130.32.0/24
- Description: VLAN pour le service de sonorisation des terrasses
- ID interne: 178

VLAN 546 - C_DANTE_LAB
- Préfixe: 10.130.34.0/24
- Description: VLAN pour le service de sonorisation du lab
- ID interne: 211

### VLANs lumière

VLAN 522 - C_LUMIERE
- Préfixe: 10.130.10.0/23
- Description: VLAN pour le système de lumière
- ID interne: 26

### VLANs vidéo et signalétique

VLAN 548 - C_VIDEO
- Préfixe: 10.130.36.0/23
- Description: VLAN pour les systèmes vidéo
- ID interne: 34

VLAN 550 - C_SIGNAGE
- Préfixe: 10.130.38.0/23
- Description: VLAN pour les systèmes de signalétique
- ID interne: 35

### VLANs d'interconnexion VRF C

VLAN 765 - C_Interco Core - Nexus
- Préfixe: 10.130.253.0/30
- Description: VLAN pour l'interconnexion entre les switch Core et Nexus
- ID interne: 36

VLAN 766 - C_Interco Core - Distr
- Préfixe: 10.130.254.0/30
- Description: VLAN pour l'interconnexion entre les switch Core et Distribution
- ID interne: 37

VLAN 767 - C_Interco Core - Fw
- Préfixe: 10.130.255.0/30
- Description: VLAN pour l'interconnexion entre les switch Core et des Firewall
- ID interne: 38

## VRF D - Téléphonie IP (10.131.0.0/16)

### VLANs téléphonie

VLAN 770 - D_PHONE_MILLENNIUM
- Préfixe: 10.131.2.0/23
- Description: VLAN pour les téléphones du Millennium
- ID interne: 39

VLAN 772 - D_ANALOG_PHONE
- Préfixe: 10.131.4.0/24
- Description: VLAN pour les téléphones analogique
- ID interne: 40

VLAN 774 - D_GUEST_PHONE
- Préfixe: 10.131.6.0/24
- Description: VLAN pour les téléphones VIP
- ID interne: 41

### VLANs services téléphonie

VLAN 962 - D_PWLAN_AutoLogin
- Description: VLAN utilisé par le service PWLAN autologin (Swisscom)
- ID interne: 147
- Note: Pas de site ni préfixe attribué

### VLANs d'interconnexion VRF D

VLAN 1021 - D_Interco Core - Nexus
- Préfixe: 10.131.253.0/30
- Description: VLAN pour l'interconnexion entre les switch Core et Nexus
- ID interne: 42

VLAN 1022 - D_Interco Core - Distr
- Préfixe: 10.131.254.0/30
- Description: VLAN pour l'interconnexion entre les switch Core et Distribution
- ID interne: 43

VLAN 1023 - D_Interco Core - Fw
- Préfixe: 10.131.255.0/30
- Description: VLAN pour l'interconnexion entre les switch Core et des Firewall
- ID interne: 44

## VRF E - Bâtiment & IoT (10.132.0.0/16)

### VLANs contrôle bâtiment

VLAN 1026 - E_BUILDING
- Préfixe: 10.132.2.0/24
- Description: VLAN pour les équipements de gestion de bâtiment
- ID interne: 45

VLAN 1028 - E_SECURITE
- Préfixe: 10.132.4.0/23
- Description: VLAN pour les équipements de sécurité
- ID interne: 46

VLAN 1030 - E_BADGE
- Préfixe: 10.132.6.0/24
- Description: VLAN pour les lecteurs de badge
- ID interne: 47

VLAN 1032 - E_SALLES
- Préfixe: 10.132.8.0/24
- Description: VLAN pour les équipements de réservation de salle
- ID interne: 48

VLAN 1034 - E_CAMERAS_IP
- Préfixe: 10.132.10.0/23
- Description: VLAN pour les caméras
- ID interne: 49

VLAN 1044 - E_ASCENCEURS
- Préfixe: 10.132.20.0/24
- Description: VLAN pour les équipements de gestion des ascenceur
- ID interne: 57

VLAN 1046 - E_PARKING
- Préfixe: 10.132.22.0/24
- Description: VLAN pour le système de caisse automatique du parking
- ID interne: 58

VLAN 1050 - E_CLIMATISATION
- Préfixe: 10.132.26.0/24
- Description: VLAN pour le système de gestion de la climatisation
- ID interne: 60

VLAN 1052 - E_SERRURES
- Préfixe: 10.132.28.0/24
- Description: VLAN pour la gestion des serrures électroniques
- ID interne: 61

VLAN 1054 - E_SAFECONTROL
- Préfixe: 10.132.30.0/24
- Description: VLAN pour les équipement d'alarme incendie
- ID interne: 62

### VLANs d'interconnexion VRF E

VLAN 1277 - E_Interco Core - Nexus
- Préfixe: 10.132.253.0/30
- Description: VLAN pour l'interconnexion entre les switch Core et Nexus
- ID interne: 50

VLAN 1278 - E_Interco Core - Distr
- Préfixe: 10.132.254.0/30
- Description: VLAN pour l'interconnexion entre les switch Core et Distribution
- ID interne: 51

VLAN 1279 - E_Interco Core - Fw
- Préfixe: 10.132.255.0/30
- Description: VLAN pour l'interconnexion entre les switch Core et des Firewall
- ID interne: 52

## VRF F - IoT & Automatisation (10.133.0.0/16)

### VLANs IoT et capteurs

VLAN 1282 - F_CAPTEURS
- Préfixe: 10.133.2.0/24
- Description: VLAN pour les capteurs IoT
- ID interne: 53

VLAN 1284 - F_AFFICHAGE_DIGITAL
- Préfixe: 10.133.4.0/24
- Description: VLAN pour l'affichage dynamique (salle de réunion)
- ID interne: 54

VLAN 1286 - F_CHROMECAST
- Préfixe: 10.133.6.0/24
- Description: VLAN pour les équipements Chromecast
- ID interne: 55

VLAN 1288 - F_DOMOTIQUE
- Préfixe: 10.133.8.0/24
- Description: VLAN pour les équipements domotique (Philips Hue, Sonos, Echo)
- ID interne: 56

VLAN 1290 - F_PRISE_ETAGES
- Préfixe: 10.133.10.0/24
- Description: VLAN pour les prise gigogne des étages et les bornes dans les bureaux
- ID interne: 87

VLAN 1292 - F_PRISE_AVL
- Préfixe: 10.133.12.0/24
- Description: VLAN pour les prise gigogne au sous-sol et la zone AVL
- ID interne: 88

VLAN 1294 - F_PRISE_OUTDOOR
- Préfixe: 10.133.14.0/24
- Description: VLAN pour les prise Gigogne à l'extérieur
- ID interne: 89

VLAN 1296 - F_SCANNETTE
- Préfixe: 10.133.16.0/24
- Description: VLAN pour les équipements de scannette (restaurant)
- ID interne: 101

VLAN 1298 - F_IMPRIMANTE_GUEST
- Préfixe: 10.133.18.0/24
- Description: VLAN pour les imprimantes des invités dans les salles de réunions
- ID interne: 102

VLAN 1300 - F_IMPRIMANTE_INTERNES
- Préfixe: 10.133.20.0/24
- Description: VLAN pour les imprimantes en interne
- ID interne: 103

VLAN 1302 - F_INFOKIOSK
- Préfixe: 10.133.22.0/24
- Description: VLAN pour les infokiosk
- ID interne: 104

VLAN 1304 - F_AIR_MEDIA
- Préfixe: 10.133.24.0/24
- Description: VLAN pour les équipements Crestron Air Media
- ID interne: 105

VLAN 1306 - F_PROJECTEUR
- Préfixe: 10.133.26.0/24
- Description: VLAN pour les projecteurs
- ID interne: 106

VLAN 1308 - F_TV
- Préfixe: 10.133.28.0/24
- Description: VLAN pour les TV
- ID interne: 107

VLAN 1310 - F_VISIO
- Préfixe: 10.133.30.0/24
- Description: VLAN pour les équipements de visioconférence
- ID interne: 108

VLAN 1312 - F_CRESTRON
- Préfixe: 10.133.32.0/24
- Description: VLAN pour les équipements Crestron
- ID interne: 111

VLAN 1314 - F_VINIBOX
- Préfixe: 10.133.34.0/24
- Description: VLAN pour les Vinibox (Guest speaker)
- ID interne: 113

VLAN 1316 - F_RASPBERRY
- Préfixe: 10.133.36.0/24
- Description: VLAN pour les Raspberry
- ID interne: 114

VLAN 1318 - F_CATERING
- Préfixe: 10.133.38.0/24
- Description: VLAN pour les équipements de catering
- ID interne: 115

VLAN 1320 - F_SUNMI
- Préfixe: 10.133.40.0/24
- Description: VLAN pour les terminaux Sunmi
- ID interne: 121

VLAN 1322 - F_PDA
- Préfixe: 10.133.42.0/24
- Description: VLAN pour les équipements PDA
- ID interne: 122

VLAN 1324 - F_POS
- Préfixe: 10.133.44.0/24
- Description: VLAN pour les terminaux POS (point of sale)
- ID interne: 123

VLAN 1326 - F_BORNES_EVENTS
- Préfixe: 10.133.46.0/24
- Description: VLAN pour les bornes événementielle
- ID interne: 130

VLAN 1328 - F_SECURITE_EVENTS
- Préfixe: 10.133.48.0/24
- Description: VLAN pour les équipements de sécurité des events
- ID interne: 131

VLAN 1330 - F_BADGEUSE
- Préfixe: 10.133.50.0/24
- Description: VLAN pour les badgeuses
- ID interne: 132

VLAN 1332 - F_LOCATION_MATERIEL
- Préfixe: 10.133.52.0/24
- Description: VLAN pour la location de matériel informatique et caisse client
- ID interne: 133

VLAN 1334 - F_WAITER
- Préfixe: 10.133.54.0/24
- Description: VLAN pour les Waiter lock
- ID interne: 149

VLAN 1336 - F_WAITER_LOCK_GUEST
- Préfixe: 10.133.56.0/24
- Description: VLAN pour les Waiter lock des invités
- ID interne: 150

VLAN 1338 - F_IFD_DOOR
- Préfixe: 10.133.58.0/24
- Description: VLAN pour les équipements de porte
- ID interne: 151

VLAN 1340 - F_GUEST_INTERNET
- Préfixe: 10.133.60.0/24
- Description: VLAN pour connexion internet direct pour les invités
- ID interne: 152

VLAN 1342 - F_GUEST_IT
- Préfixe: 10.133.62.0/24
- Description: VLAN pour se connecter au réseau Millennium lors de test
- ID interne: 153

VLAN 1344 - F_GATEWAY_LORAWAN
- Préfixe: 10.133.64.0/24
- Description: VLAN pour les gateways Lorawan
- ID interne: 227

VLAN 1346 - F_DRONE_TOIT
- Description: VLAN pour les équipements de drone sur le toit
- ID interne: 230
- Note: Pas de préfixe attribué

VLAN 1348 - F_DRONE_E0
- Description: VLAN pour les équipements de drone au E0
- ID interne: 231
- Note: Pas de préfixe attribué

### VLANs distribution multicast

VLAN 1528 - F_Distrib_S1_AVL
- Préfixe: 10.133.248.0/28
- Description: Vlan pour l'interconnexion distrib access pour Multicast VRF F
- ID interne: 112

VLAN 1529 - F_Distrib_E6_AVL
- Préfixe: 10.133.249.0/28
- Description: Vlan pour l'interconnexion distrib access pour Multicast VRF F
- ID interne: 116

### VLANs services infrastructure VRF F

VLAN 1518 - F_SAFECONTROL_SRV
- Description: VLAN pour le serveur SafeControl
- ID interne: 217
- Note: Pas de préfixe attribué

VLAN 1530 - F_FLASHBLADE
- Préfixe: 10.133.250.0/24
- Description: VLAN pour les services fournit par la FlashBlade
- ID interne: 59

### VLANs d'interconnexion VRF F

VLAN 1533 - F_Interco Core - Nexus
- Préfixe: 10.133.253.0/30
- Description: VLAN pour l'interconnexion entre les switch Core et Nexus
- ID interne: 63

VLAN 1534 - F_Interco Core - Distr
- Préfixe: 10.133.254.0/30
- Description: VLAN pour l'interconnexion entre les switch Core et Distribution
- ID interne: 64

VLAN 1535 - F_Interco Core - Fw
- Préfixe: 10.133.255.0/30
- Description: VLAN pour l'interconnexion entre les switch Core et des Firewall
- ID interne: 65

## VRF G - Guest & Événementiel (10.134.0.0/16)

### VLANs invités et clients

VLAN 1538 - G_OFFICE
- Préfixe: 10.134.2.0/23
- Description: VLAN pour les équipements informatique des invités
- ID interne: 66

VLAN 1540 - G_MJF_GUEST_INTERNET
- Préfixe: 10.134.4.0/24
- Description: VLAN pour les MJF Guest sur internet direct
- ID interne: 154

VLAN 1542 - G_MJF_GUEST_RESSOURCES
- Préfixe: 10.134.6.0/23
- Description: VLAN pour les MJF Guest sur avec accès aux ressource local
- ID interne: 155

VLAN 1544 - G_MONTREUX_MUSIC
- Préfixe: 10.134.8.0/24
- Description: VLAN pour les équipements de Montreux Music
- ID interne: 156

VLAN 1546 - G_EVENTIM
- Préfixe: 10.134.10.0/24
- Description: VLAN pour les équipements Eventim
- ID interne: 157

### VLANs événements et partenaires

VLAN 1548 - G_GUEST_AVL
- Préfixe: 10.134.12.0/24
- Description: VLAN pour les équipements AVL des invités
- ID interne: 158

VLAN 1550 - G_PARTNER_TICKETCORNER
- Préfixe: 10.134.14.0/24
- Description: VLAN pour les équipements partner TicketCorner
- ID interne: 159

VLAN 1552 - G_LOC_EXT_AVL
- Préfixe: 10.134.16.0/24
- Description: VLAN pour les équipements de location pour zone AVL
- ID interne: 160

VLAN 1554 - G_LOC_EXT_OUTDOOR
- Préfixe: 10.134.18.0/24
- Description: VLAN pour les équipements de location pour zone OUTDOOR
- ID interne: 161

VLAN 1556 - G_GUEST_LOC_AVL
- Préfixe: 10.134.20.0/24
- Description: VLAN pour les équipements des invités pour zone AVL
- ID interne: 162

VLAN 1558 - G_LOC_EXT_VOIP
- Préfixe: 10.134.22.0/24
- Description: VLAN pour les équipements de téléphonie de location
- ID interne: 163

VLAN 1560 - G_CARAVANE_TDR
- Préfixe: 10.134.24.0/24
- Description: VLAN pour les équipements de la caravane TdR
- ID interne: 164

VLAN 1562 - G_GUEST_FAIRMONT
- Préfixe: 10.134.26.0/24
- Description: VLAN pour les équipements des invités du Fairmont
- ID interne: 165

VLAN 1564 - G_GUEST_LUX
- Préfixe: 10.134.28.0/24
- Description: VLAN pour les équipements des invités du LUX
- ID interne: 166

VLAN 1566 - G_GUEST_EVENTS
- Préfixe: 10.134.30.0/24
- Description: VLAN pour les équipements des invités pour les événements
- ID interne: 167

VLAN 1568 - G_GUEST_TERRASSES
- Préfixe: 10.134.32.0/24
- Description: VLAN pour les équipements des invités pour les terrasses
- ID interne: 168

VLAN 1570 - G_GUEST_STRAV
- Préfixe: 10.134.34.0/24
- Description: VLAN pour les équipements des invités pour le Stravinski
- ID interne: 169

VLAN 1572 - G_GUEST_QG
- Préfixe: 10.134.36.0/24
- Description: VLAN pour les équipements des invités pour le QG
- ID interne: 170

VLAN 1574 - G_GUEST_AUDITORIUM
- Préfixe: 10.134.38.0/24
- Description: VLAN pour les équipements des invités pour l'auditorium
- ID interne: 171

VLAN 1576 - G_GUEST_CLUB
- Préfixe: 10.134.40.0/24
- Description: VLAN pour les équipements des invités pour le club
- ID interne: 172

VLAN 1578 - G_GUEST_LAB
- Préfixe: 10.134.42.0/24
- Description: VLAN pour les équipements des invités pour le lab
- ID interne: 173

VLAN 1580 - G_GUEST_ART_CENTER
- Préfixe: 10.134.44.0/24
- Description: VLAN pour les équipements des invités pour l'art center
- ID interne: 174

VLAN 1582 - G_GUEST_EX_SALON
- Préfixe: 10.134.46.0/24
- Description: VLAN pour les équipements des invités dans l'ex salon
- ID interne: 175

VLAN 1584 - G_ACCES_INTERNET
- Préfixe: 10.134.48.0/24
- Description: VLAN pour les bornes de location accès internet direct
- ID interne: 186

VLAN 1586 - G_GUEST_ACCES_RESSOURCES
- Préfixe: 10.134.50.0/24
- Description: VLAN pour les bornes de location avec accès aux ressources
- ID interne: 187

VLAN 1588 - G_GUEST_OFFICE_INTERNET
- Préfixe: 10.134.52.0/24
- Description: VLAN pour les équipements invité accès internet
- ID interne: 188

VLAN 1590 - G_BARILLON
- Préfixe: 10.134.54.0/24
- Description: VLAN pour les équipements AVL du Barillon
- ID interne: 189

VLAN 1592 - G_GRAND_HOTEL
- Préfixe: 10.134.56.0/24
- Description: VLAN pour les équipements AVL du Grand Hotel
- ID interne: 190

VLAN 1594 - G_GUEST_TERRASSES_I
- Préfixe: 10.134.58.0/24
- Description: VLAN pour les équipements des invités pour les terrasses indoor
- ID interne: 193

VLAN 1596 - G_GUEST_TEST
- Préfixe: 10.134.60.0/24
- Description: VLAN pour les tests AVL avec les invités
- ID interne: 194

VLAN 1598 - G_GUEST_TERRASSES_O
- Préfixe: 10.134.62.0/24
- Description: VLAN pour les équipements des invités pour les terrasses outdoor
- ID interne: 195

VLAN 1600 - G_GUEST_VIP_INTERNET
- Préfixe: 10.134.64.0/24
- Description: VLAN pour les équipements des invités VIP access internet
- ID interne: 196

VLAN 1602 - G_GUEST_VIP_RESSOURCE
- Préfixe: 10.134.66.0/24
- Description: VLAN pour les équipements VIP avec accès aux ressources
- ID interne: 197

VLAN 1604 - G_GUEST_MTECH
- Préfixe: 10.134.68.0/24
- Description: VLAN pour les équipements partner Millennium tech
- ID interne: 198

VLAN 1606 - G_DJ
- Préfixe: 10.134.70.0/24
- Description: VLAN pour les équipements DJ sur les iles
- ID interne: 199

VLAN 1608 - G_GUEST_PISCINE
- Préfixe: 10.134.72.0/24
- Description: VLAN pour les équipements AVL de la zone piscine
- ID interne: 200

VLAN 1610 - G_GUEST_STA_HOTES
- Préfixe: 10.134.74.0/24
- Description: VLAN pour les équipements AVL de la gare des hôtes
- ID interne: 202

VLAN 1612 - G_GUEST_JARDINS
- Préfixe: 10.134.76.0/24
- Description: VLAN pour les équipements AVL du jardin
- ID interne: 203

VLAN 1614 - G_GUEST_QUAI_47
- Préfixe: 10.134.78.0/24
- Description: VLAN pour les équipements AVL du quai 47
- ID interne: 204

VLAN 1616 - G_GUEST_EUREKA
- Préfixe: 10.134.80.0/24
- Description: VLAN pour les équipements AVL de l'eureka
- ID interne: 205

VLAN 1618 - G_GUEST_VOILE_BLANCHE
- Préfixe: 10.134.82.0/24
- Description: VLAN pour les équipements AVL de la voile blanche
- ID interne: 207

VLAN 1620 - G_GUEST_RTS_MJF
- Préfixe: 10.134.84.0/24
- Description: VLAN pour les équipements RTS pendant MJF
- ID interne: 208

VLAN 1622 - G_EPICERIE
- Préfixe: 10.134.86.0/24
- Description: VLAN pour les équipements AVL de l'epicerie
- ID interne: 201

VLAN 1624 - G_GUEST_INTERNET
- Préfixe: 10.134.88.0/24
- Description: VLAN pour les appareils vip to internet
- ID interne: 206

VLAN 1626 - G_GOLF
- Préfixe: 10.134.90.0/24
- Description: VLAN pour le golf
- ID interne: 214

### VLANs WiFi invités

VLAN 1728 - G_WIFI_PARTENAIRES
- Préfixe: 10.134.192.0/23
- ID interne: 137

### VLANs distribution multicast VRF G

VLAN 1784 - G_Distrib_S1_AVL
- Préfixe: 10.134.248.0/28
- Description: Vlan pour l'interconnexion distrib access pour Multicast VRF G
- ID interne: 134

VLAN 1785 - G_Distrib_E6_AVL
- Préfixe: 10.134.249.0/28
- Description: Vlan pour l'interconnexion distrib access pour Multicast VRF G
- ID interne: 135

### VLANs services infrastructure VRF G

VLAN 1786 - G_FLASHBLADE
- Préfixe: 10.134.250.0/24
- Description: VLAN pour les services fournit par la FlashBlade
- ID interne: 70

### VLANs d'interconnexion VRF G

VLAN 1789 - G_Interco Core - Nexus
- Préfixe: 10.134.253.0/30
- Description: VLAN pour l'interconnexion entre les switch Core et Nexus
- ID interne: 71

VLAN 1790 - G_Interco Core - Distr
- Préfixe: 10.134.254.0/30
- Description: VLAN pour l'interconnexion entre les switch Core et Distribution
- ID interne: 72

VLAN 1791 - G_Interco Core - Fw
- Préfixe: 10.134.255.0/30
- Description: VLAN pour l'interconnexion entre les switch Core et des Firewall
- ID interne: 73

## VRF H - Broadcast & Media (10.135.0.0/16)

### VLANs production audiovisuelle

VLAN 1802 - H_SON
- Préfixe: 10.135.2.0/24
- Description: VLAN pour les éléments son de la radio
- ID interne: 179

VLAN 1804 - H_VIDEO
- Préfixe: 10.135.4.0/24
- Description: VLAN pour les éléments vidéo de la radio / TV
- ID interne: 180

VLAN 1806 - H_OFFICE
- Préfixe: 10.135.6.0/24
- Description: VLAN pour les éléments office de la radio / TV
- ID interne: 181

VLAN 1808 - H_SIGNAGE
- Préfixe: 10.135.8.0/24
- Description: VLAN pour les éléments signage de la radio / TV
- ID interne: 182

VLAN 1810 - H_LUMIERE
- Préfixe: 10.135.10.0/24
- Description: VLAN pour les éléments Lumière de la radio / TV
- ID interne: 183

### VLANs infrastructure technique VRF H

VLAN 1812 - H_SRV_MGMT
- Préfixe: 10.135.12.0/24
- Description: VLAN pour les iLO des serveurs MMG
- ID interne: 184

VLAN 1814 - H_KVM
- Préfixe: 10.135.14.0/24
- ID interne: 216

VLAN 1816 - H_WINMEDIA_SRV
- Préfixe: 10.135.16.0/24
- Description: VLAN pour les serveurs virtuelles Winmedia
- ID interne: 218

## VRF I - MJF & MAM (10.136.0.0/16)

### VLANs Montreux Jazz Festival

VLAN 2058 - I_OFFICE
- Préfixe: 10.136.2.0/24
- Description: VLAN pour les équipements MJF / MMV
- ID interne: 224

VLAN 2060 - I_MAM_SRV
- Préfixe: 10.136.4.0/24
- Description: VLAN pour les serveurs de la solution MAM - MJF
- ID interne: 225

VLAN 2062 - I_MJF_RTS
- Préfixe: 10.136.6.0/24
- Description: VLAN pour la connexion des équipements RTS au MJF
- ID interne: 228

VLAN 2064 - I_MAM_S3
- Préfixe: 10.136.8.0/24
- Description: VLAN pour le service S3
- ID interne: 229

VLAN 2066 - I_MJF_STREAM
- Préfixe: 10.136.10.0/24
- Description: VLAN pour les équipements de streaming MJF
- ID interne: 232

### VLANs services infrastructure VRF I

VLAN 2306 - I_FLASHBLADE
- Préfixe: 10.136.250.0/24
- Description: VLAN pour le service FlashBlade sur la VRF I
- ID interne: 226

### VLANs d'interconnexion VRF I

VLAN 2308 - I_CORE_DISTR_OUTDOOR
- Préfixe: 10.136.251.0/28
- Description: VLAN d'interco pour la connexion avec la distribution extérieur
- ID interne: 223

VLAN 2309 - I_CORE_DISTR_AVL
- Préfixe: 10.136.252.0/28
- Description: VLAN d'interco pour la connexion avec la distribution AVL
- ID interne: 222

VLAN 2310 - I_CORE_DISTR_ETAGES
- Préfixe: 10.136.253.0/28
- Description: VLAN d'interco pour la connexion avec la distribution d'étages
- ID interne: 221

VLAN 2311 - I_CORE_NEXUS
- Préfixe: 10.136.254.0/28
- Description: VLAN d'interco pour la connexion avec les nexus
- ID interne: 220

VLAN 2312 - I_CORE_FW
- Préfixe: 10.136.255.0/28
- Description: VLAN d'interco pour la connexion avec le firewall
- ID interne: 219

## VRF O - DMZ & Services externes (10.142.0.0/16)

### VLANs DMZ

VLAN 3586 - O_VMSM_SRV_DMZ
- Préfixe: 10.142.2.0/24
- Description: VLAN pour les serveurs VMSM en DMZ
- ID interne: 129

VLAN 3588 - O_SBC_TEAMS
- Préfixe: 10.142.4.0/24
- Description: VLAN pour connecter le trunk SIP entre les SBC et MS Teams
- ID interne: 142

VLAN 3590 - O_FRSH_SRV_DMZ
- Préfixe: 10.142.6.0/24
- Description: Vlan pour les serveurs fresh
- ID interne: 192

### VLANs d'interconnexion VRF O

VLAN 3835 - O_Interco Core - Distrib Outdoor
- Préfixe: 10.142.251.0/28
- Description: VLAN pour l'interconnexion Core Distrib Outdoor VRF O
- ID interne: 128

VLAN 3836 - O_Interco Core - Distrib AVL
- Préfixe: 10.142.252.0/28
- Description: VLAN pour l'interconnexion Core Distrib AVL VRF O
- ID interne: 127

VLAN 3837 - O_Interco Core - Distrib Etages
- Préfixe: 10.142.253.0/28
- Description: VLAN pour l'interconnexion Core Distrib étages VRF O
- ID interne: 126

VLAN 3838 - O_Interco Core - Nexus
- Préfixe: 10.142.254.0/28
- Description: VLAN pour l'interconnexion Core Nexus VRF O
- ID interne: 125

VLAN 3839 - O_Interco Core - FW
- Préfixe: 10.142.255.0/28
- Description: VLAN pour l'interconnexion Core FW VRF O
- ID interne: 124

## VLANs sans site attribué

### Audio/Vidéo

VLAN 516 - C_AVB_STREAM
- Description: VLAN pour le flux audio / video du protocole AVB
- ID interne: 176
- Statut: Actif

### Index des VRF

VRF A (10.128.0.0/16) : Infrastructure Management
VRF B (10.129.0.0/16) : Infrastructure IT & Serveurs
VRF C (10.130.0.0/16) : Audiovisuel Production
VRF D (10.131.0.0/16) : Téléphonie IP
VRF E (10.132.0.0/16) : Bâtiment & IoT
VRF F (10.133.0.0/16) : IoT & Automatisation
VRF G (10.134.0.0/16) : Guest & Événementiel
VRF H (10.135.0.0/16) : Broadcast & Media
VRF I (10.136.0.0/16) : MJF & MAM (Montreux Jazz Festival & Media Asset Management)
VRF O (10.142.0.0/16) : DMZ & Services externes

### Convention de nommage VLANs

Préfixe VRF suivi du type de service:
- A_ : Infrastructure management
- B_ : Serveurs et IT
- C_ : Audiovisuel production
- D_ : Téléphonie
- E_ : Bâtiment
- F_ : IoT et automatisation
- G_ : Invités et événements
- H_ : Broadcast et media
- I_ : MJF et MAM
- O_ : DMZ et externe

Suffixes récurrents:
- _MGMT / _MGT : Management
- _SRV : Serveurs
- _INTERCO : Interconnexion
- _GUEST : Invités
- _LOC : Location
- _FLASHBLADE : Service de stockage Pure Storage
- _DISTR : Distribution

### Notes techniques

- Tous les VLANs sont dans un statut "Actif"
- Site principal: Millennium
- Entité: Millennium Center SA
- Les VLANs d'interconnexion utilisent généralement des /28 ou /30
- Les VLANs de production utilisent des /24 ou /23
- Chaque VRF possède ses propres VLANs d'interconnexion avec les équipements Core, Nexus, Distribution et Firewall
- Les dates de création s'échelonnent de 2020 à 2024
- Certains VLANs n'ont pas de préfixe IP attribué (notamment dans la VRF F pour les drones et SafeControl)
