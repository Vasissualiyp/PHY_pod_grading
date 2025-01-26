{
  description = "1st-year UofT course grader's flake";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs {
          inherit system;
          config = {
            allowUnfree = true;
          };
        };
        python = pkgs.python311Packages.python;
        pythonEnv = python.withPackages (ps: with ps; [
          pandas
          numpy
          openpyxl
          configparser
          selenium
          #getpass

          #csv
          #scipy
          #jupyterlab  # Include JupyterLab in pythonEnv
          #ipykernel   # Include ipykernel to register kernels        
        ]);
      in
      {
        devShell = pkgs.mkShell {
          buildInputs = with pkgs; [
            pythonEnv
            firefox
            google-chrome
          ];
        };
      }
    );
}
