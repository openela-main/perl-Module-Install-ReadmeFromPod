# Support output to PDF
%if ! (0%{?rhel})
%{bcond_without perl_Module_Install_ReadmeFromPod_enables_pdf}
%else
%{bcond_with perl_Module_Install_ReadmeFromPod_enables_pdf}
%endif

Name:           perl-Module-Install-ReadmeFromPod
Version:        0.30
Release:        4%{?dist}
Summary:        Module::Install extension to automatically convert POD to a README
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Module-Install-ReadmeFromPod/
Source0:        http://www.cpan.org/authors/id/B/BI/BINGOS/Module-Install-ReadmeFromPod-%{version}.tar.gz
# Regenerate README in UTF-8
Patch0:         Module-Install-ReadmeFromPod-0.26-Regenerate-README-in-UTF-8.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Install::AutoLicense)
BuildRequires:  perl(Module::Install::AuthorRequires) >= 0.02
BuildRequires:  perl(Module::Install::GithubMeta)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(strict)
BuildRequires:  sed
# Build script uses lib/Module/Install/ReadmeFromPod.pm
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Capture::Tiny) >= 0.05
BuildRequires:  perl(IO::All)
# Module::Install::Base version from Module::Install in Makefile.PL
BuildRequires:  perl(Module::Install::Base) >= 1
BuildRequires:  perl(Pod::Html)
BuildRequires:  perl(Pod::Man)
BuildRequires:  perl(Pod::Markdown) >= 2
BuildRequires:  perl(Pod::Text) >= 3.13
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Optional run-time:
%if %{with perl_Module_Install_ReadmeFromPod_enables_pdf}
BuildRequires:  perl(App::pod2pdf)
%endif
# Tests:
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::InDistDir)
BuildRequires:  perl(Test::More) >= 0.47
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
%if %{with perl_Module_Install_ReadmeFromPod_enables_pdf}
Suggests:       perl(App::pod2pdf)
%endif
Requires:       perl(Capture::Tiny) >= 0.05
Requires:       perl(IO::All)
# Module::Install::Base version from Module::Install in Makefile.PL
Requires:       perl(Module::Install::Base) >= 1
Requires:       perl(Pod::Html)
Requires:       perl(Pod::Man)
Requires:       perl(Pod::Markdown) >= 2
Requires:       perl(Pod::Text) >= 3.13

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Module::Install::Base\\)$

%description
Module::Install::ReadmeFromPod is a Module::Install extension that
generates a README file automatically from an indicated file containing
POD, whenever the author runs Makefile.PL. Several output formats are
supported: plain-text, HTML, PDF or manual page.

%prep
%setup -q -n Module-Install-ReadmeFromPod-%{version}
%patch0 -p1
# Remove bundled modules
rm -r inc
sed -i -e '/^inc\// d' MANIFEST
# Drop executable bit from documentation
chmod -x tools/git-log.pl

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README tools
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.30-2
- Perl 5.26 rebuild

* Mon Feb 20 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.30-1
- 0.30 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.26-2
- Perl 5.24 rebuild

* Thu Apr 28 2016 Petr Pisar <ppisar@redhat.com> - 0.26-1
- 0.26 bump

* Tue Apr 26 2016 Petr Pisar <ppisar@redhat.com> - 0.24-1
- 0.24 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.22-4
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.22-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 26 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.22-1
- 0.22 bump

* Sun Aug 04 2013 Petr Pisar <ppisar@redhat.com> - 0.20-4
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 22 2012 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-1
- 0.20 bump

* Fri Jun 22 2012 Jitka Plesnikova <jplesnik@redhat.com> 0.18-1
- Specfile autogenerated by cpanspec 1.78.
