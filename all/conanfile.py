from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout
from conan.tools.files import get


required_conan_version = ">=1.51.1"

class ConfuSociConan(ConanFile):
    name = "confu_soci"
    license = "BSL-1.0"
    description = "convenience functions for reducing boilerplate while working with socis orm feature"
    topics = "convenience function orm"
    url = "<Package recipe repository url here, for issues about the package>"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "CMakeDeps", "CMakeToolchain"



    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def configure(self):
        self.options["soci"].with_boost = True
        self.options["soci"].with_sqlite3 = True
        self.options["boost"].header_only = True

    def requirements(self):
        self.requires("soci/4.0.3", transitive_libs=True, transitive_headers=True)
        self.requires("magic_enum/[>=0.9.5 <10]", transitive_libs=True, transitive_headers=True)
        self.requires("boost/1.83.0")
        self.requires("sqlite3/3.44.2", transitive_libs=True, transitive_headers=True)

    def source(self):
        get(self, **self.conan_data["sources"][self.version],strip_root=True)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def layout(self):
        cmake_layout(self, src_folder=self.name+"-"+str(self.version))

    def package(self):
        cmake = CMake(self)
        cmake.install()



    def package_info(self):
        self.cpp_info.libs = ["confu_soci"]


