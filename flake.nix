{
  description = "wordle-qt";

  inputs.nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";

  outputs =
    inputs:
    let
      system = "x86_64-linux";
      pkgs = import inputs.nixpkgs { inherit system; };
      app = pkgs.callPackage ./default.nix { };
    in
    {
      packages.${system}.default = app;

      apps.${system}.default = {
        type = "app";
        program = "${app}/bin/wordle-qt";
      };

      devShells.${system}.default = pkgs.mkShell {
        inputsFrom = [ app ];
      };
    };
}
