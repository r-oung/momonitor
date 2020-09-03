# Momonitor

## Hardware Setup
Setup I2C:
```
sudo nano /boot/config.txt
```

Find the line containing `dtparam=i2c_arm=on` and replace the line with:
```
dtparam=i2c_arm=on,i2c_arm_baudrate=400000
```

Save the file and reboot.
