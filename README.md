# twitter_image_downloader

To download Twitter images.

## Usage

### Settings

Add yout favorite accounts to your twitter list.

Register API key in myauth.py.

### kamieshi_images.py 
```sh
	for status in api.list_timeline('ATH_ray_', 'kamieshi', count=200, page=pager):
```
Replace 'ATH_ray_', 'kamieshi' to 'Your account name', 'List name'.

```sh
python kamieshi_images.py 
```

### user_image.py

```sh
python user_image.py account_name
```
Download images of a specific account.