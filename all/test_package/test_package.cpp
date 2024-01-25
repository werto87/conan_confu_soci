#include <confu_soci/convenienceFunctionForSoci.hxx>


int main() {
  confu_soci::typeNameWithOutNamespace (Player{}) == "Player");
  return 0;
}
