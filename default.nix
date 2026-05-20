{
  pkgs ? import <nixpkgs> { },
}:

pkgs.python3Packages.buildPythonApplication {
  pname = "wordle-qt";
  version = "0";

  src = ./.;

  pyproject = true;

  build-system = with pkgs.python3Packages; [
    setuptools
  ];

  dependencies = with pkgs.python3Packages; [
    pyqt6
    wordfreq
  ];

  nativeBuildInputs = [
    pkgs.qt6.wrapQtAppsHook
  ];

  buildInputs = [
    pkgs.qt6.qtbase
  ];
}
