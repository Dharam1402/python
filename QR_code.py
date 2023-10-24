import qrcode
img = qrcode.make('https://www.youtube.com/redirect?event=channel_description&redir_token=QUFFLUhqazltcTVRZ1NJaVhzNDB3UmxDZXZZWHRvblhkd3xBQ3Jtc0tsSlZyM1hrcU1jc082T1E0SGZqSWZqem9OczZKWVFJbFRWdDFRck9DemtuT2wxemRTMFBNVXhtbU5ha3NOZldUVTFXZ2FsbnZlQTkxMXl2cjVReWM3QzFwQjU3TVNuSzZLeEZWR1dTekZJbnJUR3NPYw&q=https%3A%2F%2Fwww.instagram.com%2Ftriggeredinsaan')
img.save('qr_1.png')
img.show() 