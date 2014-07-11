# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/stack
# catalog-date 2007-02-28 00:02:05 +0100
# catalog-license lppl
# catalog-version 1.00
Name:		texlive-stack
Version:	1.00
Release:	8
Summary:	Tools to define and use stacks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/stack
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stack.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stack.source.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.00-2
+ Revision: 756165
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.00-1
+ Revision: 719575
- texlive-stack
- texlive-stack
- texlive-stack
- texlive-stack

