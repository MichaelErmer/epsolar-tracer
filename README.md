# epsolar-tracer
Tools for EPsolar Tracer A and BN solar charge controller
===================================================
![Img](img/epsolar_tracer_bn.jpg)

This is the second generation of the EPsolar Tracer solar charge controller. 
You need RS-485 adapter for communication. The first generation controller 
used RS-232 and a different protocol. see https://github.com/xxv/tracer.

[Product link 1](http://www.epsolarpv.com/en/index.php/Product/pro_content/id/573/am_id/136)  
[Product link 2](http://www.epsolarpv.com/en/index.php/Product/index/id/653/am_id/134)  

[Windows software & nice pictures](http://gwl-power.tumblr.com/tagged/tracer)

Linux driver for Exar USB UART
------------------------------
In [directory](xr_usb_serial_common-1a) there is a Linux driver for Exar based USB RS-485 adapter.  
[Original source](https://www.exar.com/common/content/default.aspx?id=10296)

Protocol
--------
[Protocol](http://www.solar-elektro.cz/data/dokumenty/1733_modbus_protocol.pdf)
See for [windows capture](archive/epsolar.txt) for some extra commands.

Python module
-------------
Uses modbus library (https://github.com/bashwork/pymodbus)  
Example output
```
# python info.py 
Manufacturer: 'EPsolar Tech co., Ltd'
Model: 'Tracer2215BN'
Version: 'V02.05+V07.12'
Charging equipment rated input voltage = 150.0V
Charging equipment rated input voltage = 150.0V
Charging equipment rated input current = 20.0A
...
```

## Raspberry (4) driver building

### Building

Readme in [xr_usb_serial_common-1a](xr_usb_serial_common-1a/README.txt)

### Raspberry 4 Issues

If your system is missing kernel headers ie. you get this error: `make[1]: *** /lib/modules/4.14.50-v7+/build: No such file or directory. Stop.`

Reinstall your bootloader, kernel and kernel-headers

```bash
sudo apt update && sudo apt install -yy --reinstall raspberrypi-bootloader raspberrypi-kernel
sudo apt install raspberrypi-kernel-headers
```

### Enabling driver

```bash
sudo rmmod cdc-acm
sudo modprobe -r cdc-acm
sudo insmod /opt/epsolar-tracer/xr_usb_serial_common-1a/xr_usb_serial_common.ko
```

### Enabling driver on boot


```
echo blacklist cdc-acm > /etc/modprobe.d/blacklist-cdc-acm.conf
update-initramfs -u
echo insmod /opt/epsolar-tracer/xr_usb_serial_common-1a/xr_usb_serial_common.ko >> /etc/rc.local
```

## MQTT

### Installation

On a modern Linux system just a few steps are needed to get the daemon working.
The following example shows the installation under Debian/Raspbian below the `/opt` directory:

```shell
git clone https://github.com/MichaelErmer/epsolar-tracer.git /opt/epsolar-tracer

cd /opt/epsolar-tracer
sudo pip3 install -r requirements.txt
```

### Configuration

To match personal needs, all operation details can be configured using the file [`config.ini`](config.ini.template).
The file needs to be created first:

```shell
cp /opt/epsolar-tracer/config.{ini.tempalte,ini}
```

### Continuous Daemon/Service

You most probably want to execute the program **continuously in the background**.
This can be done either by using the internal daemon or cron.

**Attention:** Daemon mode must be enabled in the configuration file (default).

1. Systemd service - on systemd powered systems the **recommended** option

   ```shell
   sudo cp /opt/epsolar-tracer/template.service /etc/systemd/system/tracer.service

   sudo systemctl daemon-reload

   sudo systemctl start tracer.service
   sudo systemctl status tracer.service

   sudo systemctl enable tracer.service
   ```