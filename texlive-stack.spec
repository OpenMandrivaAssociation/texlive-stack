Name:		texlive-stack
Version:	15878
Release:	2
Summary:	Tools to define and use stacks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/stack
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stack.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stack.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a small set of commands to implement
stacks independently of TeX's own stack. As an example of how
the stacks might be used, the documentation offers a small
"relinput" package that implements the backbone of the import
package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/stack/relinput.sty
%{_texmfdistdir}/tex/latex/stack/stack.sty
#- source
%doc %{_texmfdistdir}/source/latex/stack/stack.dtx
%doc %{_texmfdistdir}/source/latex/stack/stack.ins

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex source %{buildroot}%{_texmfdistdir}
