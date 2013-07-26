%define upstream_name Proc-ProcessTable
%define upstream_version 0.48

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1
Summary:	Interface to process table information
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Proc/%{upstream_name}-%{upstream_version}.tar.bz2
Patch:		Proc-ProcessTable-0.45-fix-format-errors.patch
BuildRequires:	perl-devel

%description
This module is a first crack at providing a consistent interface to
Unix (and maybe other multitasking OS's) process table information.
The impetus for this came about with my frustration at having to parse
the output of various systems' ps commands to check whether specific
processes were running on different boxes at a larged mixed Unix site.
The output format of ps was different on each OS, and sometimes
changed with each new release of an OS. Also, running a ps subprocess
from within a perl or shell script and parsing the output was not a
very efficient or aesthetic way to do things.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch -p 1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%doc README README.linux Changes TODO contrib example.pl
%{perl_vendorarch}/Proc
%{perl_vendorarch}/auto/Proc
%{_mandir}/*/*



%changelog
* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.450.0-3mdv2011.0
+ Revision: 556098
- rebuild for perl 5.12

* Thu Sep 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.450.0-2mdv2010.0
+ Revision: 429000
- fix format errors
- new perl version macro

* Thu Sep 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.45-1mdv2009.0
+ Revision: 283734
- update to new version 0.45

* Sun Aug 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.44-1mdv2009.0
+ Revision: 270395
- update to new version 0.44

* Sat Jul 19 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.43-1mdv2009.0
+ Revision: 238725
- update to new version 0.43

* Sun Jan 27 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.42-1mdv2008.1
+ Revision: 158622
- update to new version 0.42

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 0.41-3mdv2008.1
+ Revision: 151411
- rebuild for perl-5.10.0

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Aug 06 2007 Anssi Hannula <anssi@mandriva.org> 0.41-2mdv2008.0
+ Revision: 59414
- annual rebuild


* Sun Jul 09 2006 Emmanuel Andry <eandry@mandriva.org> 0.41-1mdv2007.0
- 0.41

* Fri Dec 23 2005 Anssi Hannula <anssi@mandriva.org> 0.40-1mdk
- initial Mandriva package

