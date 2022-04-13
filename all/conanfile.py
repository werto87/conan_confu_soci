import shutil
import os
from conans.tools import download, unzip, check_md5, check_sha1, check_sha256
from conans import ConanFile, CMake, tools


class ConfuSociConan(ConanFile):
    name = "confu_soci"
    license = "BSL-1.0"
    author = "werto87"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "convenience functions for reducing boilerplate while working with socis orm feature"
    topics = ("convenience function orm")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "cmake"

    @property
    def _source_subfolder(self):
        return "source_subfolder"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def configure(self):
        self.options["soci"].with_boost = True
        self.options["soci"].with_sqlite3 = True

    def requirements(self):
        self.requires("soci/4.0.2@werto87/stable")
        self.requires("magic_enum/[>=0.7.2]")

    def source(self):
        tools.get(**self.conan_data["sources"][self.version])
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self._source_subfolder)
        cmake.build()

    def package(self):
        self.copy("*.h*", dst="include/confu_soci",
                  src="source_subfolder/confu_soci")
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["convenienceFunctionForSoci"]
