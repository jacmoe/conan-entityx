from conans import ConanFile, CMake, tools


class EntityxConan(ConanFile):
    name = "EntityX"
    version = "1.2.0"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Entityx here>"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        self.run('git clone https://github.com/alecthomas/entityx.git')
        self.run('cd entityx && git checkout master')
        #self.run('cd entityx && git checkout tags/{}'.format(self.version))

    def build(self):
        cmake = CMake(self.settings)
        args = []
        args += ['-DCMAKE_INSTALL_PREFIX=install']

        self.run('cmake {}/entityx {}'.format(
                self.conanfile_directory, cmake.command_line
        ))
        self.run('cmake --build . --target install {}'.format(cmake.build_config))

    def package(self):
        self.copy('*.h', dst='include/entityx', src='entityx/entityx')
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["entityx"]
