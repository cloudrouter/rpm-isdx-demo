%define		git_commit_id	995386282931f9b3481ea4421adf5da30b22ad19
%define		isdx_build_dir	iSDX-%{git_commit_id}
%define		isdx_dest_dir	/opt/isdx-demo

%if 0%{?fedora}
%define		dist_dir	fedora
%else if 0%{?el7}
%define		dist_dir	centos
%endif

Name:		isdx-demo
Version:	1.0.0
Release:	1%{?dist}
Summary:	Industrial Scale SDX Controller (iSDX) Demo
License:	AGPLv3
Group:		Applications/Communications
URL:		http://sdx.cs.princeton.edu/

Source0:	https://github.com/sdn-ixp/iSDX/archive/%{git_commit_id}.tar.gz
Source1:	virtualbox-repo.tar.gz

Requires:	vagrant
Requires:	VirtualBox-5.0

BuildArch:	noarch

%description
iSDX Demo provides a runnable demo of the Industrial Scale SDX Controller (iSDX)

%prep
%setup -n %{isdx_build_dir}
%setup -T -D -b 1 -c -n %{isdx_build_dir}

%build

%install
install -d %{buildroot}%{isdx_dest_dir}
cp -R %{_builddir}/%{isdx_build_dir}/* %{buildroot}%{isdx_dest_dir}

# VirtualBox GPG Key & RPM Repo
mkdir -p -m 755 %{buildroot}%{_sysconfdir}/pki/rpm-gpg
install -Dpm 644 %{_builddir}/%{isdx_build_dir}/oracle_vbox.asc %{buildroot}%{_sysconfdir}/pki/rpm-gpg

mkdir -p -m 755 %{buildroot}%{_sysconfdir}/yum.repos.d
install -pm 644 %{_builddir}/%{isdx_build_dir}/%{dist_dir}/virtualbox.repo %{buildroot}%{_sysconfdir}/yum.repos.d

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/opt/isdx-demo/*
%config(noreplace) /etc/yum.repos.d/virtualbox.repo
/etc/pki/rpm-gpg/oracle_vbox.asc

%changelog
* Tue Feb 02 2016 John Siegrist <jsiegrist@iix.net> - 1.0.0-1
- Initial release of the the RPM package.
