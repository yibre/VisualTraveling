# VisualTraveling
Visual Traveling by KAIST 2021 Spring Introduction to Human Computer Interection team project - by Visual Traveler

# Hosting cite: http://yibre.gabia.io/

# Team Member
* 20140762 YunCheol Ha
* 20186651 Doyeon Choi
* 20214902 Xiangchi Song
* 20214903 Letian Zhang

---
# Implementation
## Tools
* Django
* Tailwind CSS

## Backend Tables
#### user
| id    | email | language | country | password |
| ----- | ----- | ---- | ---- | ---- |
| int | char | char | char | char |

#### post
| id    | title | author | location_info | picture |
| ----- | ----- | ---- | ---- | ---- |
| int | char | char | char | char |

#### photo
| id | post | file | caption |
| ---- | ---- | ---- | ---- |
| int | post | file | char |

#### List
| user | id | posts |
| ---- | ---- | ---- |
| user | int | post |

## Pages:
Every HTML files that we used is in
visualtravel > templates > posts folder

### Main Page:
![image](https://user-images.githubusercontent.com/36833349/119801399-a39c9380-bf18-11eb-846e-f3731aca0fdf.png)
html files in this page:
base.html: The logo, search, upload button, my list button
post_card.html: it's for each post card, especially the photo, title, camera inforamtion, location information, my list add button
post_list.html: To add the main banner("find the place and get inspired") and align each post card

### Search Engine:
![image](https://user-images.githubusercontent.com/36833349/119803159-26721e00-bf1a-11eb-9817-546293e7d1a2.png)
html files in this page:
base.html, post_card.html
search.html: to get the query of search keyword and show the result that fit with the keyword

### Upload Post:
![image](https://user-images.githubusercontent.com/36833349/119803497-794bd580-bf1a-11eb-9b2f-ea5409708a97.png)
html files in this page:
base.html
post_detail.html: it shows photo, and contents of the post, the map that where the photo was taken

### Favorite List:
![image](https://user-images.githubusercontent.com/36833349/119804262-27577f80-bf1b-11eb-84dc-9fe123d7a6af.png)
html files in this page:
base.html, post_card.html
fav_list.html: to align the post cards that users added

### Upload, edit Post:
html files in this page: post_form.html, post_create.html, photo_create.html, post_photos.html
post_create.html: to upload the post, they have to fill the form of it.
post_photos.html: It's the page to see the photo list of each post
photo_create.html: Adding the caption and upload file page
post_form.html: to edit the post, users have to fill the form of it.



