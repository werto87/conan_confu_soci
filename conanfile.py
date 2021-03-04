import shutil
import os
from conans.tools import download, unzip, check_md5, check_sha1, check_sha256
from conans import ConanFile, CMake, tools


class ConfuSociConan(ConanFile):
    name = "confu_soci"
    version = "0.2.0"
    license = "BSL-1.0"
    author = "werto87"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "convenience functions for reducing boilerplate while working with socis orm feature"
    topics = ("convenience function orm")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "cmake"
    scm = {
        "type": "git",
        "subfolder": "confu_soci",
        "url": "https://github.com/werto87/confu_soci.git",
        "revision": "main"
    }

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def configure(self):
        self.options["soci"].with_boost = True
        self.options["soci"].with_sqlite3 = True

    def requirements(self):
        self.requires("boost/1.75.0")
        self.requires("soci/4.0.1")
        self.requires("magic_enum/0.6.6")
        self.requires("sqlite3/3.34.1")
        self.requires("catch2/2.13.1")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="confu_soci")
        cmake.build()

    def package(self):
        self.copy("*.h*", dst="include/confu_soci",
                  src="confu_soci/confu_soci")
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["convenienceFunctionForSoci"]
