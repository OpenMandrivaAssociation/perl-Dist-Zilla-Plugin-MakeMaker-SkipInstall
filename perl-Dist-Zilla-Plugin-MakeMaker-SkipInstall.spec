%define upstream_name    Dist-Zilla-Plugin-MakeMaker-SkipInstall
%define upstream_version 1.100

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Skip the install rule of MakeMaker
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Dist::Zilla)
BuildRequires:	perl(Dist::Zilla::Plugin::CheckChangeLog)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
This small plugin will edit the 'Makefile.PL' file, and override the
install target to become a no-op.

This will make your module fail the install phase. It will be built, and
tested but will never be installed.

The most common use for this techinique is for the Task manpage modules.
Without a proper install phase, you can install your Task module repetedly.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
#make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

