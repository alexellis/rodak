# rodak

Build your own Rodak - a portable camera powered by your Raspberry Pi.

Bring a new perspective to your photography with your very own retro camera shooting from waist-level instead of eye-level. Thanks to the built-in ground, glass this is also a low-powered project that doesn't need a separate electronic screen.

[Follow me on Twitter @alexellisuk](https://twitter.com/alexellisuk) and [read my latest Raspberry Pi tutorials on my blog](https://blog.alexellis.io/tag/raspberry-pi/) with loads of cool hacks and weekend projects.

> As [featured on Adafruit.com](https://blog.adafruit.com/2018/09/28/build-your-own-rodak-a-portable-camera-powered-by-your-raspberry-pi-raspberry_pi-piday-raspberrypi-alexellisuk/)

## Video 

https://www.instagram.com/p/BoD8Va7gfQViHKyGVmXas5B9YHIgMke6-ouJkg0/?taken-by=alexellisuk

![The front](https://discourse-cdn-sjc1.com/business6/uploads/pimoroni/optimized/2X/6/6cdba6f5f155242ea1179845a020a81203351e2e_1_666x500.jpeg)

![Internals](https://pbs.twimg.com/media/Dn8KtNBWsAEhzWA.jpg:small)

![Shooting](https://pbs.twimg.com/media/Dn8Rgm_WsAIhAT1.jpg:small)

## Sample photos & build photos

See the whole Twitter thread for all the sample and build photos:

https://twitter.com/alexellisuk/status/1044521342941491200

## Parts list

* Enclosure

This can be an old Kodak Brownie repurposed, or a $1 clear plastic lunch-box from a thrift store such as Poundland. My Brownie cost around 8GBP from eBay, but I also found some in a local charity shop.

* Raspberry Pi Zero W & 32GB SD card - flashed with Raspbian Lite

* Small LiPo battery - [Pimoroni](https://shop.pimoroni.com/)

* Either Pimoroni Zero LiPo battery shim or Adafruit PowerBoost 1000C

* [RTC DS3231 module](https://thepihut.com/products/mini-rtc-module-for-raspberry-pi?variant=758601217)

[RTC Installation](https://raspberrytips.nl/ds3231-rtc-raspberry-pi/)

* Single NeoPixel for indicating status (ready to take photo/taking photo)

* Raspberry Pi Camera V2

* [Momentary push button](https://cpc.farnell.com/multicomp/r13-509a-05-br/switch-push-button-spno-mom/dp/SW04283) for the shutter

* Tilt switch for setting EXIF orientation data automatically.

Additional parts for assembly: soldering iron, solder, heat-shrink wrap, hot glue gun and double-sided adhesive velcro.


## Code

See the [src](src) folder for my Python code.

You can use cron and an `@reboot` line to automatically start the software.
