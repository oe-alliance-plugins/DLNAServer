from setuptools import setup
import setup_translate

pkg = 'Extensions.DLNAServer'
setup(name='enigma2-plugin-extensions-dlnaserver',
       version='3.0',
       description='this is dlna server using minidlna',
       package_dir={pkg: 'DLNAServer'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
