%global tl_name stack
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.00
Release:	%{tl_revision}.1
Summary:	Tools to define and use stacks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/stack
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/stack.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/stack.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a small set of commands to implement stacks
independently of TeX's own stack. As an example of how the stacks might
be used, the documentation offers a small "relinput" package that
implements the backbone of the import package.

