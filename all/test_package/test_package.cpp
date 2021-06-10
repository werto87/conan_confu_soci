#include <confu_soci/convenienceFunctionForSoci.hxx>
#include <iostream>

BOOST_FUSION_DEFINE_STRUCT((test), EasyClass,
                           (std::string, playerId)(double, points))

int main() {
  std::cout << confu_soci::structAsString(test::EasyClass{}) << std::endl;
}
